import requests
import json
import os
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader

from airflow.models import Variable
from airflow.hooks.mysql_hook import MySqlHook
from airflow.hooks.S3_hook import S3Hook



def get_valerios_last_games() -> dict:
    """
    We will get valerios1910 previous day chess games.
    """
    chess_com_endpoint = Variable.get('CHESS_COM_ENDPOINT')

    prev_day = datetime.now() - timedelta(days=1)  # Get the previous day
    url = f"{chess_com_endpoint}valerios1910/games/{prev_day.year}/{'{:02d}'.format(prev_day.month)}"
    games = requests.get(url).json()['games']

    for game in games:
        game_time = datetime.utcfromtimestamp(game['end_time'])

        # Keep only the last day games
        if prev_day.day == game_time.day:
            if game["white"]["username"] == "valerios1910":
                val_color = "white"
                val_res = game["white"]
                opp_res = game["black"]
            else:
                val_color = "black"
                val_res = game["black"]
                opp_res = game["white"]

            white_user = game["white"]["username"]
            yield {
                "datetime": game_time.strftime('%Y-%m-%d %H:%M:%S'),
                "result": val_res['result'],
                "color": val_color,
                "opp_username": opp_res['username'],
                "time_control": game['time_class'],
                "opp_rating": opp_res['rating']
            }


def fill_sql_table():
    insert_game_query = """
        INSERT INTO chess_db.MatchHistory (
            OpponentUsername,
            OpponentRating,
            Result,
            TimeControl,
            StartDatetime, 
            Color)
        VALUES (%s, %s, %s, %s, %s, %s); 
        """

    for game in get_valerios_last_games():
        sql_hook = MySqlHook(mysql_conn_id='chess_db')
        sql_hook.run(sql=insert_game_query,
                        parameters=tuple([
                            game['opp_username'],
                            game['opp_rating'],
                            game['result'],
                            game['time_control'],
                            game['datetime'],
                            game['color'],
                        ]))


def get_games_from_db_and_render_html(**context):
    columns = ("opp_username", "opp_rating", "result", "time_control", "datetime", "color")
    select_query = """
        SELECT OpponentUsername, OpponentRating, Result, TimeControl, StartDatetime, "Color"
        FROM chess_db.MatchHistory;
        """
    sql_hook = MySqlHook(mysql_conn_id="chess_db")
    rows = sql_hook.get_records(select_query)

    games = [dict(zip(columns, row)) for row in rows]
    
    root = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(root))
    template = env.get_template("email.html")

    html_content = template.render(games=games)

    # Store the html file as airflow metadata using Xcom
    task_instance = context["task_instance"]
    task_instance.xcom_push(key="chess_report_html_content", value=html_content)


def write_html_report_to_s3(**context):
    hook = S3Hook(aws_conn_id="s3_report_bucket")
    print("HEREE")
    task_instance = context["task_instance"]
    print(task_instance)
    print(task_instance.xcom_pull(task_ids='get_games_and_render_html', \
                         key='chess_report_html_content'))

    hook.load_string(
        string_data=task_instance.xcom_pull(task_ids='get_games_and_render_html', \
                         key='chess_report_html_content'),
        key=f"chess_reports/valerios_chess_report_{datetime.now().strftime('%Y_%m_%d')}",
        bucket_name=Variable.get("CHESS_S3_BUCKET"),
        replace=True,
    )