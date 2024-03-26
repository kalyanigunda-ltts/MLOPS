from  src.mlProject import logging
print('Hi ....smile')
from src.mlProject import logger,logging
from src.mlProject.pipeline.stage_data_ingestion01 import DataIngestionTrainingPipeline

STAGE_NAME = 'data Ingestion Stage'

logging.info('Welcome to our Custom Logging')
try:
    logger.info(f'>>>>stage {STAGE_NAME} started')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>stage {STAGE_NAME} COMPLETED <<<<\n\nx=========x')
except Exception as e:
    logger.exception(e)
    raise e