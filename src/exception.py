import sys
import logging


#exc_info : is execution information. it will give us 3 information, that exc_tb is important for us
#it will shows from which file which line i will probably get exception
def error_message_detail(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()
    #custome exception handling from documentation of exception python
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno,str(error))
    
    return error_message
    

#error detail track by sys and the instance variable is error message. 
class customException(Exception):
    def __init__(self, error_message, error_detail:sys):
        
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        super().__init__(error_message)
#once we found the error we will share and print message. we use this in every place we need it.

    def __str__(self):
        return self.error_message
# if __name__ =='__main__':
#     try:
#         a=1/0
#     except Exception e:
#         logging.info("logging started")
#         raise customException(e, sys)
# if __name__ =='__main__':
#     try:
#         a=1/0
#     except Exception as e: # <--- 1. Capture the exception object 'e'
#         logging.info("logging started")
        
#         # 2. Pass 'e' as the error_message and the system module 'sys' as error_detail
#         #    Note: 'e' here represents the 'ZeroDivisionError' instance.
#         raise customException(e, sys)

import logging
import sys
# ... (rest of your functions and classes)

if __name__ == '__main__':
    # You need to ensure logging is configured before this block runs.
    # If your logger.py is set up, you should import the configured logger.

    try:
        a = 1 / 0
    except Exception as e:
        # 1. Instantiate the custom exception class to get the formatted message
        custom_error = customException(e, sys)
        
        # 2. Log the formatted message at the ERROR level
        logging.error(custom_error.error_message) 
        
        # 3. Then, re-raise the exception to terminate the program
        raise custom_error # It's better practice to raise the instantiated object