"""
## Mini projeto de ETL utilizando o Airflow para orquestrar a extração de data de vendas de jogos de video game.
"""

from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator

import os
import kagglehub
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

@dag(
    start_date=datetime(2025, 1, 6),
    schedule="30 2 6 * *",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3, "retry_delay": timedelta(seconds=30)},
    tags=["video-games", "s3", "soda"],
)
def airflow_video_game_sales():
    @task
    def extract():
        directory_path = kagglehub.dataset_download("asaniczka/video-game-sales-2024")
        file_path = os.path.join(directory_path, "vgchartz-2024.csv")

        df_video_game_sales = pd.read_csv(
            file_path,
            header=0,
        )

        return df_video_game_sales
    
    @task
    def transform(data: pd.DataFrame):
        if data.empty:
            raise ValueError("Sem data para transformar")

        data["title"] = data["title"].dropna()
        data["release_date"] = data["release_date"].dropna()

        data = data.drop("last_update", axis=1)
        data = data.loc[
            (data.publisher != "Unknown") & 
            (data.developer != "Unknown") & 
            (data.critic_score > 8)
        ]
        
        file_path = '/tmp/dataframe.parquet'
        data.to_parquet(file_path, index=False)
        
        return file_path

    data = extract()
    transformed_data = transform(data)

    bucket_name = os.getenv("BUCKET_NAME")
    key = os.getenv("KEY")

    create_bucket = S3CreateBucketOperator(
        task_id="create_bucket",
        bucket_name=bucket_name,
        region_name="us-east-1",
    )

    create_object = LocalFilesystemToS3Operator(
        task_id="load",
        filename=transformed_data,
        dest_key=key,
        dest_bucket=bucket_name,
        replace=True,
    )
    
    create_bucket >> create_object

airflow_video_game_sales()

