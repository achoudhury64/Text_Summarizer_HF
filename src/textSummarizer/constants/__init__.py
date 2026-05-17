#basically we are defining the paths for the config and params files. 
# Why is it important? Because we will be using these paths in our code to read the config and params files.
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
