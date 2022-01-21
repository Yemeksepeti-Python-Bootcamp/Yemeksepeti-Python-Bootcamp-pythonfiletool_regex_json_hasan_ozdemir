"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from argparse import ArgumentParser
from sys import argv

class HelperDb:

    def __init__(self) -> None:
        """
        This constructor is created to get named command line args.
        return : None
        """
        # initialize Argument parser
        parser=ArgumentParser()
        # prepare named arguments
        parser.add_argument('--file',help='Json file path',type=str)
        parser.add_argument('--db',help='Database file path',type=str)
        # get the named command line arguments
        self.json_path=parser.parse_args().file
        self.db_path=parser.parse_args().db
