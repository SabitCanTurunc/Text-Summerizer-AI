import os
from box.exceptions import BoxValueError
import yaml
from textSummerizer.logging import Logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If YAML file is empty.

    Returns:
        ConfigBox: ConfigBox object containing YAML content.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            Logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("Invalid YAML format")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"YAML file '{path_to_yaml}' not found")
    except Exception as e:
        raise e


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB

    Args:
        path (Path): Path to the file.
    
    Returns:
        str: size in KB
        """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"