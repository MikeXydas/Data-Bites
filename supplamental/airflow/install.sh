# The official installation script by https://airflow.apache.org/docs/apache-airflow/stable/start/local.html

# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=2.1.0
PYTHON_VERSION=3.8
# For example: 3.6
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.1.0/constraints-3.6.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# initialize the database
airflow db init

airflow users create \
    --username Mike \
    --firstname Mike \
    --lastname Xydas \
    --role Admin \
    --email mikexydas@gmail.com


### A set of useful commands for reference ###

# Command to run the webserver
# airflow webserver --port 8080

# Run the scheduler
# airflow scheduler

# Test a task of a tag separately
# airflow tasks test chess_progress_report fill_sql_table 2021-06-04