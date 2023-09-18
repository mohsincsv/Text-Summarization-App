import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s]')

project_name = "textSummarizerApp"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for filepath in list_of_files:
    path = Path(filepath)

    filedir, filename= os.path.split(path)

    # If file already exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Directory: {filedir} for the file {filename}")
    # If file does not exist or is empty
    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {path}")

    else:
        logging.info(f"{filename}")