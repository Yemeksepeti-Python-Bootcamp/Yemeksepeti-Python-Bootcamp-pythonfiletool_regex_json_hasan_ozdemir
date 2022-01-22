
import os
import logging
import logging.handlers


#TODO all methods content TBD
class ProjectLogging:

    def __init__(self) -> None:
        pass

    def successful_log(self)-> None:
        pass

    def value_error_log(self)->None:
        pass

    def missing_arg_log(self)-> None:
        pass

    def file_not_found_log(self,error_msg:str)->logging.getLogger():
        log_format="%(levelname)s %(asctime)s -> %(message)s"
        logging.basicConfig(filename="../project_logs.log",
                            filemode="w",
                            format=log_format,
                            level=logging.ERROR)

        logger_obj = logging.getLogger()
        return logger_obj.error(error_msg)
    
if __name__=='__main__':
    log_obj=ProjectLogging()