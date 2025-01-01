from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


default_args = {
    'owner': 'tanzid',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG (
    dag_id="bash_dag_v3",
    default_args = default_args,
    description="This is first dag",
    start_date=datetime(2024, 12, 30),
    schedule_interval='@daily'
) as dag :
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello world, this is the second task following first task'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hello world, this is the third task following first task with second task'
    )

    task1.set_downstream(task2)
    task3.set_upstream(task1)

