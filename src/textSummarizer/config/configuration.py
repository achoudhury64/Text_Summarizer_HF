from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    #This method is the constructor of the class. It takes two parameters: config_path and params_path, which are paths to the configuration and parameters YAML files, respectively.
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    #This method retrieves the data ingestion configuration from the configuration file and creates the necessary directories. and returns the data ingestion configuration.

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

#the DataIngestionConfig is a dataclass that is defined in the constants file. It is used to store the configuration for the data ingestion process.
        #Why do we define it in the constants file? Because we want to make sure that the configuration is consistent across the project.
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

