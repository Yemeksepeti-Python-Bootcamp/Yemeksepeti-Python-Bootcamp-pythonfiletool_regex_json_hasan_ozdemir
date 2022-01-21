"""
This script is created to manage database opeations 
@Hasan Özdemir 01/21/2022
"""

import sqlite3 as sql
from helper import HelperDb


class Database(HelperDb):

    def __init__(self) -> None:
        # inherit from HelperDb class
        HelperDb.__init__(self)

    # if you want to test in further you can use this built-in method
    def __str__(self) -> list:
        return [self.json_path,self.db_path]
        

    def push_data_to_db(self):
        pass


if __name__=='__main__':
    db_object=Database()
    print(db_object.__str__())

# how to run 
# open cmd in current project folder
# test_case1: python main.py --file hasan.db --db hasan.db
# test_case2: python main.py --file hasan1.db --db hasan1.db