import os
import sys
from zipfile import ZipFile
from Hate_Speech_Classification.logger import logging
from Hate_Speech_Classification.exception import CustomException
from Hate_Speech_Classification.configuration.gcloud_operations import GCloudSync
from Hate_Speech_Classification.entity.config_entity import DataIngestionConfig
from Hate_Speech_Classification.entity.artifact_entity import DataIngestionArtifacts

class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync()

    def get_data_from_gcloud(self):
        try:
            logging.info("Entered the get_data_from gcloud method of data ingestion")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,exist_ok=True)

            self.gcloud.sync_folder_from_gcloud(self.data_ingestion_config.BUCKET_NAME,
                                                self.data_ingestion_config.ZIP_FILE_NAME,
                                                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
            
            logging.info("Exited the get_data_from gcloud method of data ingestion")
            
        except Exception as e:
            logging.info("Error occurred during data ingestion")
            raise CustomException(e,sys)
        
    def unzip_and_clean(self):
        logging.info("Entered the unzip and clean method")
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH,"r") as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Exited the unzip and clean method")

            return self.data_ingestion_config.DATA_ARTIFACTS_DIR, self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR
            
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Started data ingestion")
        try:
            self.get_data_from_gcloud()
            logging.info("It has downloaded data from gcloud")
            imbalance_data_file_path,raw_data_file_path = self.unzip_and_clean()

            data_ingestion_artifacts = DataIngestionArtifacts(imbalance_data_file_path,raw_data_file_path)
            logging.info("Successfully done")

            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e,sys)
