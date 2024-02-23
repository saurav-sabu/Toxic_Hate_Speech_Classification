import sys
from Hate_Speech_Classification.logger import logging
from Hate_Speech_Classification.exception import CustomException
from Hate_Speech_Classification.components.data_ingestion import DataIngestion
from Hate_Speech_Classification.entity.config_entity import DataIngestionConfig
from Hate_Speech_Classification.entity.artifact_entity import DataIngestionArtifacts

class Training_Pipeline:

    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Getting the data from gcloud")

        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data")
            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def run_pipeline(self):
        logging.info("Entered the run pipeline")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys)
