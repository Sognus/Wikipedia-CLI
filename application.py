# Python libraries imports
import os
from datetime import datetime, timedelta

# 1st party imports
from parsing import *
from db.models import *

# 3rd party imports
import cmd2


# Commandline application
class WikipediaApplication(cmd2.Cmd):

    def __init__(self):
        # Call parent initialization
        super().__init__()

        # Set commandline prefix to >
        self.prompt = "> "

    """
        COMMAND "CLEAR" AND ITS SUBCOMMANDS
    """

    # Command clear
    @cmd2.with_argparser(argparse_clear)
    def do_clear(self, args):
        func = getattr(args, 'func', None)
        if func is not None:
            # Call selected subcommand function
            func(self, args)
        else:
            if os.name == "posix":
                # Unix/Linux/MacOS/BSD/etc
                os.system('clear')
            else:
                # Windows
                os.system('cls')

    # Clear subcommands
    def clear_history(self, args):
        # Delete entire history if input number is less than 1
        if args.count < 1:
            self.history.clear()
        else:
            # Remove certain number of elements from history based on input value
            del self.history[:args.count]

    def clear_cache(self, args):
        # Delete entire searchcache
        WikipediaData.objects.all().delete()
        self.poutput("Cache was cleared.")

    def clear_help(self, args):
        self.do_help("clear")

    # Set handlers for subcommands
    argparse_clear_history.set_defaults(func=clear_history)
    argparse_clear_help.set_defaults(func=clear_help)
    argparse_clear_cache.set_defaults(func=clear_cache)

    """
        COMMAND "SEARCH" AND ITS SUBCOMMANDS
    """

    @cmd2.with_argparser(argparse_search)
    def do_search(self, args):
        # Transform text from list to continuous string
        text = ' '.join([str(part) for part in args.text])

        # Query data from local cache
        time_threshold = datetime.now() - timedelta(days=7)
        data = WikipediaData.objects.filter(name=text, cached_at__gt=time_threshold).first()

        # If data from local cache were not found, perform API search and cache
        if data is None:
            data = WikipediaData()
            data.fill_model_from_api(text)
            data.cached_at = datetime.now()
            data.save()

        # Print
        self.poutput(data.summary)

    """
        COMMAND "SEARCH" AND ITS SUBCOMMANDS
    """

    def do_stop(self, args):
        self.poutput("Stopping the application..")
        return True

    def do_exit(self, args):
        self.poutput("Stopping the application..")
        return True