"""
Formatting of the logs can be customized here. 
For now, we will use a simple format that includes the timestamp, logger name, log level, and message.
"""
import logging 

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(message)s"
        )
     