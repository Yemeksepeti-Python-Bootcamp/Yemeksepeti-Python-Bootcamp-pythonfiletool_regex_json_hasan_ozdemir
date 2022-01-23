
import os
import logging
import logging.handlers


#TODO all methods content TBD
class ProjectLogging:

    def __init__(self) -> None:
        # format the output
        self.log_format="LEVEL_NAME : %(levelname)s || %(asctime)s || CODE_LINE : %(lineno)d || MESSAGE : %(message)s"
        # default settings for each logging level
        logging.basicConfig(filename="../project_logs.log",
                            filemode="a",
                            format=self.log_format)
        self.log_obj = logging.getLogger()

    # CRITICAL LEVEL 50
    def critical_log(self,error_msg,str)->None:
        self.log_obj.setLevel(logging.INFO)
        self.log_obj.info(error_msg)

    # ERROR LEVEL 40
    def error_log(self,error_msg:str)->None:
        self.log_obj.setLevel(logging.ERROR)
        self.log_obj.error(error_msg)

    # INFO LEVEL 20
    def info_log(self,log_msg:str)-> None:
        self.log_obj.setLevel(logging.INFO)
        self.log_obj.info(log_msg)
    
if __name__=='__main__':
    log_obj=ProjectLogging()
    log_obj.info_log('Hasan')