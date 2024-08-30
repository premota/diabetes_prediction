from src.config.config_manager import ConfigManager
from src.utils.util import read_yaml
from yaml_config.yaml_path import PIPELINE_CONFIG_PATH

def test():
    obj = ConfigManager()
    schema = obj.get_schema_validation_config()
    schema =schema.data_schema_validation
    print(schema)


if __name__ == "__main__":
    test()
