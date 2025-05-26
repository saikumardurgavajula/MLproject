import sys
import logging

def error_message_details(error, error_detail: sys):
    """
    Extracts filename, line number, and original error message
    from the current exception context and formats them.
    """
    _, _, exc_tb = error_detail.exc_info()         # capture the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # script name
    line_number = exc_tb.tb_lineno                  # line number
    # use an f-string (you could also use .format(file_name, line_number, error))
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] error message [{error}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_details: sys):
        # call the base Exception init with the raw error message
        super().__init__(str(error))
        # build and store our richer message
        self.error_message = error_message_details(error, error_details)

    def __str__(self):
        return self.error_message


