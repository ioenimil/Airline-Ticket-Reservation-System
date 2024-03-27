import re

def validate_name(name):
    # Regular expression pattern to match a valid name
    pattern = r'^[A-Za-z\s\'-]+$'
    # ^ : Start of the string
    # [A-Za-z] : Match any uppercase or lowercase letter
    # \s : Match any whitespace character (space, tab, newline)
    # \' : Match apostrophe
    # - : Match hyphen
    # + : Match one or more occurrences of the preceding pattern
    # $ : End of the string

    # Compile the regular expression pattern
    regex = re.compile(pattern)

    # Check if the name matches the pattern
    if regex.match(name):
        return True #returns True if name is valid 
    else:
        return False #returns False if name is invalid 


