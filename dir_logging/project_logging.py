
import os
import logging
import logging.handlers


class ProjectLogging:

    def __init__(self,log_file:str) -> None:
        """
        This constructor is created to initialize logger object and format the log output
        :param log_file: <str> path of log file to write
        """
        # format the output
        self.log_format="LEVEL_NAME : %(levelname)s || %(asctime)s || CODE_LINE : %(lineno)d || MESSAGE : %(message)s"
        # default settings for each logging level
        logging.basicConfig(filename=log_file,
                            filemode="a",
                            format=self.log_format)
        # create logger object
        self.log_obj = logging.getLogger()

    # CRITICAL LEVEL 50
    def critical_log(self,error_msg:str)->None:
        """
        This method is created to log critical level of logs when it's raised
        :param error_msg: <str> Error message
        :return: None
        """
        self.log_obj.setLevel(logging.INFO)
        self.log_obj.info(error_msg)

    # ERROR LEVEL 40
    def error_log(self,error_msg:str)->None:
        """
        This method is created to log error level of logs when it's raised
        :param error_msg: <str> Error message
        :return: None
        """
        self.log_obj.setLevel(logging.ERROR)
        self.log_obj.error(error_msg)

    # INFO LEVEL 20
    def info_log(self,info_msg:str)-> None:
        """
        This method is created to log info level of logs when it's successfully done
        :param log_msg: <str> Error message
        :return: None
        """
        self.log_obj.setLevel(logging.INFO)
        self.log_obj.info(info_msg)
    
if __name__=='__main__':
    log_obj=ProjectLogging()
    log_obj.info_log('Hasan')