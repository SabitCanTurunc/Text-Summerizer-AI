from textSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummerizer.logging import logger

STAGE_NAME = "Data Ignestion stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx================================x")

except Exception as e:
    logger.exception(e)
    raise e 