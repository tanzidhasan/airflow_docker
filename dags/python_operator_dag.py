from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta


default_args = {
    'owner': 'tanzid',
    'retries': 5,
    'retry_delay': timedelta(minutes=3)
}

def name(name):
    print(f"My name is {name}. ")

def age(age):
    print(f"I am {age} years old.")

with DAG (
    dag_id="python_operator_dag_v3",
    default_args=default_args,
    description="This is a python operator dag",
    start_date=datetime(2024, 12, 30),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="name",
        python_callable=name,
        op_kwargs={"name": "Tanzid"}
    )

    task2 = PythonOperator(
        task_id="age",
        python_callable=age,
        op_kwargs={"age": 26}
    )

    task1 >> task2

