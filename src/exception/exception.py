import sys
from src.logging import logger

class Networksecurityexception(Exception):
    def __init__(self,error_massage,error_details:sys):
        self.error_massage=error_massage
        _,_,exc_tb=error_details.exc_info()
        

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error oceured in python script name [{0}] line number [{1}]error massage [{2}]".format(self.file_name,self.lineno,str(self.error_massage))




