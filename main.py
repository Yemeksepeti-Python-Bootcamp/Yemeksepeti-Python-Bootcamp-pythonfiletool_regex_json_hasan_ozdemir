# import packages
from argparse import ArgumentParser
from sys import argv
import sqlite3 as sql


class Database:

    def __init__(self) -> None:
        # initialize Argument parser
        parser=ArgumentParser()
        # prepare named arguments
        parser.add_argument('--file',help='Json file path',type=str)
        parser.add_argument('--db',help='Database file path',type=str)
        # get the named command line arguments
        self.json_path=parser.parse_args().file
        self.db_path=parser.parse_args().db

    # if you want to test in further you can use this built-in method
    def __str__(self) -> list:
        return [self.json_path,self.db_path]
        

    def read_data(self):
        pass


if __name__=='__main__':
    db_object=Database()
    print(db_object.__str__())

# how to run 
# open cmd in current project folder
# test_case1: python main.py --file hasan.db --db hasan.db
# test_case2: python main.py --file hasan1.db --db hasan1.db