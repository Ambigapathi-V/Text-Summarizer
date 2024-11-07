from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_ingestion import DataIngestion
from src.TextSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        # Load configuration
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)

        data_ingestion.download_file()

        data_ingestion.extract_zip_file()