import sys

def get_error_details(errormsg,error:sys):
    _,_,exc_tab = error.exc_info()

    filename = exc_tab.tb_frame.f_code.co_filename
    errormessage = "Error occured at srcipt name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tab.tb_lineno,str(errormsg)
        )

    return errormessage
class WaferException(Exception):
    def __init__(self,errormessage,error:sys):
        
        super().__init__(errormessage)

        self.error = get_error_details(errormessage,error)

    def __str__(self) -> str:
        return self.error