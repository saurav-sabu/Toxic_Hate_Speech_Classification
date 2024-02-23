import os
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
ARTIFACTS_DIR: str = os.path.join("artifacts",TIMESTAMP)
BUCKET_NAME: str = "hate-speech-data"
ZIP_FILE_NAME : str = "dataset.zip"
LABEL: "label"
TWEET: "tweet"

DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"



