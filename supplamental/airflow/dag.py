from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator
# from airflow.operators.mysql_operator import MySqlOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {
    "owner": "Mike",
    "depends_on_past": False,
    "start_date": datetime(2021, 6, 1),
    "email": ["mikexydas@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "@daily",
}

with DAG("chess_progress_report", default_args=default_args) as dag:
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
            `Won` BOOLEAN,
            `TimeControl` VARCHAR(50),
            `StartDatetime` DATETIME,
            `Color` VARCHAR(10),
            PRIMARY KEY (`GameId`)
        )
        """
    )

    Task_Create_Table
