# Updating the configuration manager

from textSummarizerApp.constants import *
from textSummarizerApp.entity import Data_Ingestion_Config
from textSummarizerApp.utils.common import read_yaml, create_directories


class Configuration_Manager:
    def __init__(self, config_path = str(CONFIG_FILE_PATH),
        params_path = str(PARAMS_FILE_PATH)):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> Data_Ingestion_Config:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = Data_Ingestion_Config(
            root_dir = config.root_dir,
            source_url = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config