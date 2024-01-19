import os
import json
import pendulum
from airflow import DAG
from asyncio import tasks
from textwrap import dedent
from airflow.operators.python import PythonOperator
from src.pipeline.batch_prediction import BatchPredictionConfig,SensorBatchPrediction

with DAG(
    'batch_prediction',
    default_args={'retries': 2},
    # [END default_args]
    description='gemstone batch prediction',
    schedule_interval="@weekly",
    start_date=pendulum.datetime(2024,1, 19, tz="UTC"),
    catchup=False,
    tags=['example'],
) as dag:

    def download_files(**kwargs):
        bucket_name = os.getenv("BUCKET_NAME")
        input_dir = "/app/input_files"
        #creating directory
        os.makedirs(input_dir,exist_ok=True)
        os.system(f"aws s3 sync s3://{bucket_name}/inbox {config.inbox_dir}")

    def batch_prediction(**kwargs):
        from src.pipeline.prediction_pipeline import PredictPipeline,CustomData
        config = PredictPipeline()
        diamond_batch_prediction = predict(features=config)
        diamond_batch_prediction.get_data_as_dataframe()
       
    def upload_files(**kwargs):
        bucket_name = os.getenv("BUCKET_NAME")
        os.system(f"aws s3 sync {config.archive_dir} s3://{bucket_name}/archive")
        os.system(f"aws s3 sync {config.outbox_dir} s3://{bucket_name}/outbox")


    download_input_files  = PythonOperator(
            task_id="download_file",
            python_callable=download_files

    )

    generate_prediction_files = PythonOperator(
            task_id="prediction",
            python_callable=batch_prediction

    )

    upload_prediction_files = PythonOperator(
            task_id="upload_prediction_files",
            python_callable=upload_files

    )

    download_input_files >> generate_prediction_files >> upload_prediction_files
