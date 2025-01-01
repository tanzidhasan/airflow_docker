from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


default_args = {
    'owner': 'tanzid',
    'retries': 5,
    'retry_delay': timedelta(minutes=3)
}


with DAG(
    dag_id='scheduler_dag_with_cron_exp_v5',
    default_args=default_args,
    description="This is scheduler dag with cron expression",
    start_date=datetime(2024, 12, 25),
    schedule_interval='22 09 * * SUN,MON'

) as dag:
    task1 = BashOperator(
        task_id='my_name',
        bash_command="echo My Name is Md. Tanzid Hasan"
    )

    task1