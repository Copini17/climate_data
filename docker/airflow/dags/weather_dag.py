from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 6, 6),
    'retries': 1
}

with DAG(dag_id='spark_to_postgres_dag', default_args=default_args, schedule_interval='@daily') as dag:

    start = DummyOperator(task_id='start')

    spark_job = SparkSubmitOperator(
        task_id='run_spark_job',
        application='',
        conn_id='spark_default',
        conf={'master': 'spark://spark:7077'},
        verbose=1
    )

    load_to_postgres = PostgresOperator(
        task_id='load_to_postgres',
        postgres_conn_id='postgres_default',
        sql="""
        
        """
    )

    start >> spark_job >> load_to_postgres