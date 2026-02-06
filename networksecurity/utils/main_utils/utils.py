import os, sys, dill, pickle, yaml, numpy as np

from networksecurity.exception.exception import NetworkSecuritySystemException
from networksecurity.logging.logger import logging

def read_yaml_file(file_path: str) -> dict:
  try:
    with open(file_path, "rb") as yaml_file:
      return yaml.safe_load(yaml_file)
  except Exception as e:
    raise NetworkSecuritySystemException(e, sys) from e
    