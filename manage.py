#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

# Set the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebookstore_project.settings')
    try:
# Try to import execute_from_command_line function from django.core.management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
# If ImportError is raised, show an informative error message
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
# Call the execute_from_command_line function with the arguments passed in sys.argv
    execute_from_command_line(sys.argv)

# If this file is run as the main program, call the main function
if __name__ == '__main__':
    main()
