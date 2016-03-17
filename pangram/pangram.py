from string import ascii_lowercase as alphabet

def is_pangram(wrd):
    return set(alphabet).issubset(set(wrd.lower()))
