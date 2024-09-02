from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen= True)
class DataExtractionConfig:
    source_url: str
    prefix: str
    local_data_file: Path
    local_load_dir: Path


@dataclass(frozen = True)
class DataSchemaConfig:
    data_schema_validation: dict
    data: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    transformation_artifact_file: Path
    target_feature: str
