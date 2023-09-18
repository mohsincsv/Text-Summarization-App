from textSummarizerApp.config.configuration import Configuration_Manager
from textSummarizerApp.components import Data_Ingestion
from textSummarizerApp.logging import logger


# Creating the pipline
# First need to initialize the configuration manager
# After ingesting the data, 


class Data_Ingestion_Pipline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = Data_Ingestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_file()