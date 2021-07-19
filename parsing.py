# 3rd party imports
import cmd2

"""
    ARGPARSE FOR COMMAND "CLEAR" AND ITS SUBCOMMANDS
"""

# Create argument parser for command "clear"
argparse_clear = cmd2.Cmd2ArgumentParser()
argparse_clear_subparsers = argparse_clear.add_subparsers(title='subcommands', help='subcommand help')

# Create argument parser for subcommands of command "clear"
argparse_clear_history = argparse_clear_subparsers.add_parser('history', help='Clears the command history')
argparse_clear_history.add_argument('count', nargs="?", default=-1)

argparse_clear_cache = argparse_clear_subparsers.add_parser("cache", help="Clears search cache")
argparse_clear_help = argparse_clear_subparsers.add_parser('help', help='Prints the clear subcommand help')

""" 
    ARGPARSE FOR COMMAND "SEARCH" AND ITS SUBCOMMANDS
"""

# Create argument parser for command "search"
argparse_search = cmd2.Cmd2ArgumentParser()
argparse_search.add_argument("--ignore-cache", dest="cache_ignored", action="store_true", default=False, help="Forces search to load ")
argparse_search.add_argument("text", nargs="+")