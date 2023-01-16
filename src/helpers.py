import re

def extract_otp(s):
    """ Extract OTP from a string
    
        s:          string
        returns:    5 digit OTP code
    """
    
    r = re.compile(r'\d\d\d\d\d')
    otp = r.search(s)
    return otp.group()