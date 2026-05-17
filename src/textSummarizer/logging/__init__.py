"""
Purpose: This setup ensures all application events are logged both to a file (logs/continuos_logs.log)
 and displayed in the console, with detailed formatting including timestamps and module information.


"""
import os
import sys
import logging

log_dir="logs"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_filepath = os.path.join(log_dir,"continuos_logs.log")
"""Creates the logs directory if it doesn't exist
exist_ok=True prevents error if directory already exists"""

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        
        logging.FileHandler(log_filepath), #Writes logs to file
        logging.StreamHandler(sys.stdout) #Displays logs in console
    ]
)

logger=logging.getLogger("summarizerlogger")