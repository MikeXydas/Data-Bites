from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago

from utils import fill_sql_table, get_games_from_db_and_render_html


default_args = {
    "owner": "Mike",
    "depends_on_past": False,
    "email": ["mikexydas@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
        "chess_progress_report", 
        default_args=default_args,
        schedule_interval="24 10 * * *",
        start_date=days_ago(2)
    ) as dag:
    # _____ Creating the table on which we will store the match history results _____
    Task_Create_Table = MySqlOperator(
        task_id="create_mysql_table",
        mysql_conn_id="chess_db",
        sql="""
        DROP TABLE IF EXISTS chess_db.MatchHistory;
        CREATE TABLE chess_db.MatchHistory (
            `GameId` INT NOT NULL AUTO_INCREMENT,
            `OpponentUsername` VARCHAR(250),
            `OpponentRating` INT,
            `Result` VARCHAR(50),
            `TimeControl` VARCHAR(50),
            `StartDatetime` DATETIME,
            `Color` VARCHAR(10),
            PRIMARY KEY (`GameId`)
        )
        """
    )

    # _____ Filling the table with the last day games _____
    Task_Fill_Table = PythonOperator(
        task_id="fill_sql_table",
        python_callable=fill_sql_table
    )

    # _____ Get the games from the db and render the html file _____
    Task_Render_Html_Results = PythonOperator(
        task_id="get_games_and_render_html",
        python_callable=get_games_from_db_and_render_html
    )

    Task_Send_Email = EmailOperator(
        task_id="send_match_report",
        to="mikexydas@gmail.com",
        subject="Valerios1910 chess results on {{ yesterday_ds }}",
        html_content="{{ task_instance.xcom_pull(task_ids='get_games_and_render_html', \
                         key='chess_report_html_content') }}",
    )

    Task_Create_Table >> Task_Fill_Table >> Task_Render_Html_Results >> Task_Send_Email
