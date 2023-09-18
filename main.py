from textSummarizerApp.pipeline.stage01_data_ingestion import Data_Ingestion_Pipline
from textSummarizerApp.logging import logger

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"{STAGE_NAME} - STARTED")
    data_ingestion = Data_Ingestion_Pipline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} - COMPLETED")
except Exception as e:
    logger.exception(e)
    raise e