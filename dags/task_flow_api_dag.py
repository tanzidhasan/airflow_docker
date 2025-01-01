from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'tanzid',
    'replies': 5,
    'reply_delay': timedelta(minutes=5)
}

@dag(
    dag_id='task_flow_api_dag_v2',
    default_args=default_args,
    description='This is task flow api dag that reduce the LOC of data sharing via XCom',
    start_date=datetime(2024, 12, 30),
    schedule_interval='@daily'
)

def student_dag():
    
    @task()
    def student(first_name, last_name, id):
        print(f"Student Name is {first_name} {last_name} " 
                f"with id {id}. ")
    
    @task(multiple_outputs=True)
    def getName():
        return {
            'first_name': 'Tanzid',
            'last_name': 'Hasan'
        }
    
    @task()
    def getId():
        return '2405016'

    name = getName()
    id = getId()

    student(name['first_name'], name['last_name'], id)

instance = student_dag()