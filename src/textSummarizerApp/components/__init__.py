# Update the components

import os
import urllib.request as request
import zipfile
from textSummarizerApp.entity import Data_Ingestion_Config
from textSummarizerApp.utils.common import get_size
from textSummarizerApp.logging import logger
from pathlib import Path


class Data_Ingestion:
    def __init__(self, config: Data_Ingestion_Config):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file {filename} with information \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    def unzip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
