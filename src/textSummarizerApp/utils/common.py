# Utils are used to write common functions that can be used across the application

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizerApp.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(filepath: str) -> ConfigBox:
    """
    This function reads and returns yaml file
    
    Args: 
        filepath: path to yaml file

    Raises:
        ValueError: if file is empty
        e: empy file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(filepath) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {filepath} loaded successfully")
            
        return ConfigBox(content)
    
    except FileNotFoundError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise ValueError(f"Error reading yaml file: {filepath}") from e

@ensure_annotations
def create_directories(dir_path: list, verbose=True):
    """
    Create a list of directories

    Args:
        dir_path: list of directory paths
        ignore log(bool, optional): if True, log will be printed. Defaults to True
    """

    for path in dir_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB

    Args:
        path: path to file

    Returns:
        str: size in KB
    """

    sizeinKB = round(os.path.getsize(path) / 1024)
    return f"~ {sizeinKB} KB"
