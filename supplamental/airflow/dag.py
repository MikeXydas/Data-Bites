from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator
