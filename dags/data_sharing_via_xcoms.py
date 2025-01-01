from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta



default_args = {
    'owner' : 'tanzid',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def student(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    id = ti.xcom_pull(task_ids='get_id')
    print(f"Student Name is {first_name} {last_name} " 
            f"with id {id}. "
            f"He/she is {age} years old. ")
    

def getName(ti):
    ti.xcom_push(key='first_name', value='Tanzid')
    ti.xcom_push(key='last_name', value='Hasan')

def getId():
    return '2405016'


with DAG (
    dag_id='data_sharing_via_xcoms_v4',
    default_args=default_args,
    description="This is a data sharing dag between tasks via xcoms",
    start_date=datetime(2024, 12, 30),
    schedule_interval="@daily"
) as dag:
    
    task1 = PythonOperator(
        task_id="get_student",
        python_callable=student,
        op_kwargs={'age': 26}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=getName
    )

    task3 = PythonOperator(
        task_id='get_id',
        python_callable=getId
    )

    [task2, task3] >> task1