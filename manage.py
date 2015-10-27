#!/usr/bin/env python
import os
import sys
from testconf import settings_shell

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_shell.__name__)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
