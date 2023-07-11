from CNN_Cat_health_classifier import logger
from CNN_Cat_health_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage | {STAGE_NAME} | Started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage | {STAGE_NAME} | Finished \n\n ========================================")
except Exception as e:
    logger.exception(f">>>>> Stage | {STAGE_NAME} | Failed")
    raise e