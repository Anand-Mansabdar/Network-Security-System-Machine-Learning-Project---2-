import sys
from networksecurity.logging import logger

import sys

class NetworkSecuritySystemException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(str(error_message))

        _, _, exc_tb = error_details.exc_info()

        self.error_message = error_message
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in python script name "
            f"[{self.file_name}] "
            f"line number [{self.lineno}] "
            f"error message [{self.error_message}]"
        )

  
if __name__ == "__main__":
  try:
    logger.logging.info("Entered the try block")
  except Exception as e:
    raise NetworkSecuritySystemException(e, sys)
