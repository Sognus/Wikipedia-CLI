# Python libraries imports
import sys
import os

# 3rd party imports
import wikipedia
import django


# Django specific settings

sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Ignore warnings caused by 3rd party library
import warnings
from bs4 import GuessedAtParserWarning
warnings.filterwarnings('ignore', category=GuessedAtParserWarning)

# 1st Party imports
from application import WikipediaApplication


# Application entry point
if __name__ == '__main__':
    # Set wikipedia language
    wikipedia.set_lang("cs")

    # Start CLI application
    app = WikipediaApplication()
    # Wait for
    exit_code = app.cmdloop()
    sys.exit(exit_code)
