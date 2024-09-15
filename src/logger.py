import logging
import os
from datetime import datetime as dt

class Logger:
    def __init__(self) -> None:
        self.LOG_FILE = f"{dt.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

    def log(self, log_message:str):
        logs_path = os.path.join(os.getcwd(), "LOGS", self.LOG_FILE)
        os.makedirs(logs_path, exist_ok=True)
        LOG_FILE_PATH = os.path.join(logs_path, self.LOG_FILE)
        
        logging.basicConfig(
            filename=LOG_FILE_PATH,
            format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO,
        )

        # Log the message
        logging.info(log_message)

# if __name__ == "__main__":
#     # Instantiated Logger Class
#     logger = Logger()
#     logger.log("Logging has started")
