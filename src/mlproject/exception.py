import sys
from src.mlproject.logger import logging

def error_message_detail(error, error_detail: sys):
    
    # Step 1: traceback object nikalo
    _, _, exc_tb = error_detail.exc_info()
    
    # Step 2: file name nikalo
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Step 3: formatted message banao
    error_message = (
        f"Error in script: [{file_name}] "
        f"line: [{exc_tb.tb_lineno}] "
        f"message: [{str(error)}]"
    )
    
    return error_message


class CustomException(Exception):
    
    def __init__(self, error_message, error_details: sys):
        # __init__ → jab object banta hai tab chalta hai
        
        super().__init__(error_message)  
        # ← parent Exception class ko bhi initialize karo
        
        self.error_message = error_message_detail(
            error_message, error_details
        )
        # ← detailed message store karo (file + line + message)
    
    def __str__(self):
        # __str__ → jab print() ya str() call hota hai tab chalta hai
        return self.error_message
        # ← ye detailed message print hoga, normal exception nahi