import os 
import sys
import logging

logging_str = "[%(asctime)s : %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "runnings_logs.log")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textsummarizationlogger")
