from text_Summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_Summarization.logging import logger


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} completed successfully <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n \n x=========x")

except Exception as e:
    logger.exception(e)