from dataclasses import dataclass
from pathlib import Path

# below looks similatly to the config file data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path