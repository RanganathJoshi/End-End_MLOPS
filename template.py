import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s: ')

project_name="mlproject"
list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipleine.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    "requirements.txt",
    "setup.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep"
]

for file in list_of_file:
    filepath=Path(file)
    dir,file_name=os.path.split(filepath)

    if dir!="":
        os.makedirs(dir,exist_ok=True)
    
    if (not os.path.exists(file)) or os.path.getsize(file)==0:
        with open(file,'w') as f:
            pass
    else:
        print("file already exsists")