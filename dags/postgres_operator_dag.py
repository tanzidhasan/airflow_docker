from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'tanzid',
    'retries': 5,
    'retry_delay': timedelta(minutes=3)
}

with DAG (
    dag_id='postgres_operator_dag_v3',
    default_args=default_args,
    description="This is postgres operator dag which uses DBeaver's postgres database",
    start_date=datetime(2024, 12, 25),
    schedule_interval='25 10 25-27 12 *'
) as dag:
    task1 = PostgresOperator(
        task_id='create_student_table',
        postgres_conn_id='postgres_localhost',
        sql="""
                CREATE TABLE if not exists dag_runs(
                    ds date,
                    dag_id character varying,
                    primary key (ds, dag_id)
                )
            """
    )

    task2 = PostgresOperator(
        task_id='insert_data_into_student_table',
        postgres_conn_id='postgres_localhost',
        sql="""
                INSERT INTO dag_runs (ds, dag_id) VALUES ('{{ds}}', '{{dag.dag_id}}')
            """
    )

    task1 >> task2