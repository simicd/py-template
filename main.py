
# Set default level above which info will be captured
import logging
logging.getLogger().setLevel(logging.INFO)

import pytemplate


result = pytemplate.template_function("World")
print(result)