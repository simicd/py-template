
import logging
from typing import List, Dict

# # Initialize logger - get package root name (e.g. __name__ = mypackage.utils -> mypackage)
logger = logging.getLogger(__name__.split(".")[0])


class JsonFormatter(logging.Formatter):
    def __init__(self, attributes: List[str], time_format: str="%Y-%m-%dT%H:%M:%S", msec_format: str='%s.%03dZ', rename: Dict[str, str]=None):
        """Define custom JSON logging formatter.

        Args:
            attributes: List of logging attributes to be written to JSON
            time_format: Python datetime format string
            msec_format: Milisecond format
            rename: Dictionary of attributes to renamed when written to JSON
        """

        # Set default JSON time format, e.g. "2020-02-12T21:27:05.092Z"
        self.default_time_format = time_format
        self.default_msec_format = msec_format
        self.attributes = attributes
        self.rename = rename
        # Import package to convert dictionary to proper JSON-formatted string
        from json import dumps
        self.dumps = dumps

    def format(self, record) -> str:
        """Define how to log record is translated to string.

        This function is defined in logging.Formatter and is overriden here
        with a custom implementation that returns JSON.

        Returns:
            Record as JSON string
        """

        attr_dict = record.__dict__
        # Convert time from UNIX to string
        attr_dict['asctime'] = self.formatTime(record)
        # Reassign name from 'msg' to 'message' to match typical formatter name
        attr_dict['message'] = attr_dict['msg']
        attr_dict = {k:v for k,v in attr_dict.items() if k in self.attributes}
        for from_name, to_name in self.rename.items():
            attr_dict[to_name] = attr_dict.pop(from_name)
        # Convert dictionary to JSON string
        return self.dumps(attr_dict)


# # Print log in JSON format
json_log_formatter = JsonFormatter(['asctime', 'module', 'levelname', 'message', 'params'], rename={'asctime': 'time', 'levelname': 'level'})

# Log outputs in console
stream_handler = logging.StreamHandler()          # Get stream handler (console output)
stream_handler.setFormatter(json_log_formatter)   # Use JSON formatter
logger.addHandler(stream_handler)                 # Activate log handler

# Log outputs as file
file_handler = logging.FileHandler('package.log')
file_handler.setFormatter(json_log_formatter)
logger.addHandler(file_handler)
