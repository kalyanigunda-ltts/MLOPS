#Entity is the return type format
from dataclasses import dataclass
from pathlib import Path

from src.mlProject.constants import *
from src.mlProject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.mlProject.utils.common import read_yaml, create_directories

#defining dataclass, Python Class vs DataClass is in python class self required but data class is variable defined
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL : str
    local_data_files :Path
    unzip_dir : Path

