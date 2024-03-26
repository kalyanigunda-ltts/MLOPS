from src.mlProject.constants import *
from src.mlProject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.mlProject.utils.common import read_yaml, create_directories
from src.mlProject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH,schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,local_data_files=config.local_data_files,unzip_dir=config.unzip_dir)
        return DataIngestionConfig