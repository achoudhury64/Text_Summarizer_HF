from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Hello Welcome to Text Summarizer Project")

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"-------------------{STAGE_NAME} started -------------------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"-------------------{STAGE_NAME} completed -------------------")
except Exception as e:
    logger.exception(e)
    raise e