import os
import sys
from box.exceptions import BoxValueError
import yaml
from src.TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and convert it to a ConfigBox.
    
    Args:
    path_to_yaml (Path): The path to the YAML file.
    
    Returns:
    ConfigBox: A ConfigBox containing the parsed YAML data.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"YAML file: {path_to_yaml} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file: {path_to_yaml}, {e}")
        sys.exit(1)

@ensure_annotations
def create_directories(path_to_directories: List[str], verbose: bool = True) -> None:
    """
    Create directories if they do not exist.
    
    Args:
    path_to_directories (List[str]): A list of paths to directories.
    verbose (bool): Whether to print the creation status of each directory.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory: {path} created successfully")

@ensure_annotations
def get_size(path:Path) -> str:
    """
    Get the size of a file or directory in bytes, kilobytes, or megabytes.
    
    Args:
    path (Path): The path to the file or directory.
    
    Returns:
    str: The size of the file or directory in bytes, kilobytes, or megabytes.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb}"