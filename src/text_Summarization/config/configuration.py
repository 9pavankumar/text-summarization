from text_Summarization.constants import *
from text_Summarization.utils.common import read_yaml, create_directories
from text_Summarization.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        
        data_ingestion_config =  DataIngestionConfig(
            root_dir = self.config.artifacts_root,
            source_url = self.config.source_url,
            local_data_file = self.config.local_data_file,
            unzip_dir = self.config.unzip_dir
        )
        return data_ingestion_config