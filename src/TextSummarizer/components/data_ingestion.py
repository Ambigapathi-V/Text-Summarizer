import os
import urllib.request as request
import zipfile
from src.TextSummarizer.entity import DataIngestionConfig
from src.TextSummarizer.logging import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"Downloaded file {filename} to {self.config.local_data_file}, size: {os.path.getsize(self.config.local_data_file)} bytes")
            else:
                logger.info(f"Local data file {self.config.local_data_file} already exists.")
        except Exception as e:
            logger.error(f"Error downloading file from {self.config.source_URL}: {e}")

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            
            logger.info(f"Attempting to extract zip file: {self.config.local_data_file}")
            
            
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted zip file to {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Failed to unzip file {self.config.local_data_file}: {e}")
        except FileNotFoundError as e:
            logger.error(f"File not found: {self.config.local_data_file}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during file extraction: {e}")