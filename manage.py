#!/usr/bin/env python
import os
import sys

import dotenv


if __name__ == '__main__':
    # Load a .env file
    dotenv.load_dotenv(dotenv.find_dotenv())

    # Set up configuration modules
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    configuration_name = os.getenv('ENVIRONMENT', 'Development')
    os.environ.setdefault('DJANGO_CONFIGURATION', configuration_name)

    # Call the Django command
    from configurations.management import execute_from_command_line
    execute_from_command_line(sys.argv)
