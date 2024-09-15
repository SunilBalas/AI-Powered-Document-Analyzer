import sys

class Messages:
    def __init__(self, error:str, error_detail:sys) -> None:
        self.error = error
        self.error_detail = error_detail
        self.message = self.error_message_detail()
    
    def error_message_detail(self) -> str:
        '''
            Format an error message with error type and details.

            Returns:
                str: A formatted error message containing the error and details.
        '''
        _, _, exc_tb = self.error_detail.exc_info() # exc_tb contains on which file and on which line exception occurred
        filename = exc_tb.tb_frame.f_code.co_filename
        
        error_message = "Error occurred in {0}, line: {1}, error message: {2}".format(
            filename,
            exc_tb.tb_lineno,
            str(self.error)
        )
        return error_message
    
class CustomException(Exception):
    def __init__(self, error_message:str, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = Messages(error=error_message, error_detail=error_detail)
        
    def __str__(self) -> str:
        return self.error_message
