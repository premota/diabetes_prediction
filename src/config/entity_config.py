from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen= True)
class DataExtractionConfig:
    source_url: str
    prefix: str
    local_data_file: Path
    local_load_dir: Path
    