import traceback
from datetime import datetime

def get_exception_message(message, exception, service: str = "parsedoc"):
    if not message:
        message = "Something is wrong! Please try again!"
    exception_msg = f"[P{service.upper()}] || [{message}] ||> [{datetime.today().strftime('%d-%m-%Y %H:%M:%S')}][Error] {str(exception).upper()} : {traceback.format_exc()}"
    return exception_msg
