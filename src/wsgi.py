import os

import dotenv


# Load a .env file
dotenv.load_dotenv(dotenv.find_dotenv())

# Set up configuration modules
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
configuration_name = os.getenv('ENVIRONMENT', 'Development')
os.environ.setdefault('DJANGO_CONFIGURATION', configuration_name)

# Acquire the WSGI app
from configurations.wsgi import get_wsgi_application  # noqa
application = get_wsgi_application()
