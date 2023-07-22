from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
logger.info("Yo! This is my custom log")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"---------Stage {STAGE_NAME} commenced!---------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"---------Stage {STAGE_NAME} completed!---------")
except Exception as e:
    logger.exception(e)
    raise e