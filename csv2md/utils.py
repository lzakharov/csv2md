import string

def column_letter(index):
    """Returns the column letter in Excel format."""
    letters = string.ascii_lowercase
    count = len(letters)
    return letters[index % count] * ((index // count) + 1)
