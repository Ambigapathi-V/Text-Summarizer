import os
import logging
import sys

# Define the logging format
logging_str = "[%(asctime)s - %(filename)s - %(funcName)s - line %(lineno)d - %(levelname)s - %(message)s]"
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format=logging_str,  # Set the logging format
    handlers=[
        logging.StreamHandler(sys.stdout),  # Log to console
        logging.FileHandler(log_filepath)   # Log to file
    ]
)

logger = logging.getLogger('textSummarizerLogger')