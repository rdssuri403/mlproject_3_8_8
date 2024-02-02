import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
logs_directory = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_directory, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_path = os.path.join(logs_directory, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)