"""
This script is created to manage dir_database opeations
@Hasan Özdemir 01/21/2022
"""

import sqlite3 as sql
from contextlib import contextmanager
from helper_db import HelperDb
from dir_logging.project_logging import ProjectLogging
from dir_constants.project_constants import LOG_PATH

class Database(HelperDb,ProjectLogging):

    def __init__(self) -> None:
        # inherit from HelperDb class
        HelperDb.__init__(self)
        ProjectLogging.__init__(log_file=LOG_PATH)

    # if you want to test in further you can use this built-in method
    def __str__(self) -> list:
        return [self.json_path,self.db_path]

    @contextmanager
    def connect_database(self,database:str)->None:
        """
        This method created to connect to database with context manager decorator
        :param database: <str> path of database
        :return: None
        """
        #instantiate connection obj __init__ method
        connect_obj=None

        connect_obj=sql.connect(
            database=database
        )
        try:
            # connect to database __enter__ method
            yield connect_obj
            self.info_log('Database connection successful')
        except Exception as connection_err:
            # rollback chances
            connect_obj.rollback()
            self.critical_log(str(connection_err))
        finally:
            # close connection __exit__ method
            connect_obj.close()
            self.info_log('Database connection closed')

    def create_automatic_table(self):
        table_name=f"customer_{self.time_formatting()}"

    def push_data_to_db(self,database:str,table_name:str):
        # todo documentation tbd
        with self.connect_database(database=database) as connection:
            pass

if __name__=='__main__':
    db_object=Database()
    #print(db_object.__str__())


# how to run 
# open cmd in current project folder
# test_case1: python main.py --file hasan.db --db hasan.db
# test_case2: python main.py --file hasan1.db --db hasan1.db