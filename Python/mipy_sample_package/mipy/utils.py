"""
Collection of simple tools we have come to need during the semester.
"""


def pretty_print(d: dict, indent=0, c=" ") -> None:
    """Recursively pretty-prints a dictionary
    
    Args:
        d (dict): dictionary to be printed
        indent (int, optional): starting indentation. Defaults to 0
        c (str): whitespace string used for indenting. Defaults to " "
    """
    white = indent * c
    for key, val in d.items():
        if type(val) == dict:
            print(white + "{}: {{".format(key))
            pretty_print(val, indent + 1, c)
            print(white + "}")
        else:
            print(white + "{}: {}".format(key, val))
            
            
def str_to_bool(instr: str) -> bool:
    """Convert common string representations of bool to bool
    
    String "y", "yes", "t", "true" (case insensitive) are converted to True.
    Everything else to False.
    
    Args:
        instr (str): input string to be converted
        
    Returns:
        bool
    """
    return instr.strip().lower() in ["y", "yes", "t", "true"]


def count_vowels(word: str) -> int:
    """Counts vowels in a given word or a sentence
    
    Args:
        word (str): input word or sentence
    
    Return:
        int: number of vowel in word
    """
    count = 0
    for c in word:
        if c in "aeiyou":
            count += 1
                
    return count
