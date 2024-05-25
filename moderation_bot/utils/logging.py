# logging.py

import logging
import os

# Set up logging configuration
log_format = '%(asctime)s - %(levelname)s - %(message)s'
log_level = logging.INFO

# Check if logs directory exists, if not, create it
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Configure logging to both console and file
logging.basicConfig(level=log_level, format=log_format, handlers=[
    logging.StreamHandler(),
    logging.FileHandler(os.path.join(logs_dir, 'bot_log.log'))
])

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)