#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.environ.get('ONHEROKU') == 1:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoutsHerokuProject.settings.prod")
        print "Prod Settings"
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoutsHerokuProject.settings.dev")
        print "Dev Settings"
        DEBUG = 'TRUE'
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
