import os   
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

#This is the data validation class which is the main conponent which does the data validation. 
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    #if files are not available, set validation_status to False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    #if files are available, set validation_status to True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
            #this is saved to the data_validation/status.txt file
            return validation_status
            
        except Exception as e:
            raise e