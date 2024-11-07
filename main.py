from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f".........Starting {STAGE_NAME}")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f"{STAGE_NAME} completed successfully......")
        
except Exception as e:
    logger.error(f"Error occurred in {STAGE_NAME}: {str(e)}")
    raise e
