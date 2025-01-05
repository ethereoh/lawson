import yaml
from typing import Any


def read_yaml(file_path: str) -> Any:
    "Reads a YAML file and returns its contents as a Python object."
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error reading YAML file: {e}")


def write_yaml(data: Any, file_path: str) -> None:
    "Writes a Python object to a YAML file."
    try:
        with open(file_path, "w") as file:
            yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False)
    except yaml.YAMLError as e:
        raise ValueError(f"Error writing YAML file: {e}")
