"""
## Mini projeto de ETL utilizando o Airflow para orquestrar a extração de dados de vendas de jogos de video game.
"""

from airflow.decorators import dag, task
from datetime import datetime

import os
import kagglehub
import pandas as pd

@dag(
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
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
    
    extract()

airflow_video_game_sales()

