import re

def cleanString (s):
    if(s is None):
        return ""

    return re.sub(r'[^a-zA-Z0-9]','',s).upper()
