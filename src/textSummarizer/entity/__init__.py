from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path #root directory for data ingestion   return type is Path
    source_URL: str #source URL for data ingestion  return type is str
    local_data_file: Path #local data file for data ingestion  return type is Path
    unzip_dir: Path #unzip directory for data ingestion  return type is Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
