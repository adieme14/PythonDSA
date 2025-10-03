def remove_single_char(s, char_to_remove):
    """
    Recursively removes all occurrences of a specified character from a string.

    Args:
        s (str): The input string.
        char_to_remove (str): The character to be removed.

    Returns:
        str: The new string with all occurrences of char_to_remove removed.
    """
    # Base Case: If the string is empty, return an empty string.
    if not s:
        return ""

    # Recursive Step:
    # If the first character is the one to be removed, skip it.
    if s[0] == char_to_remove:
        return remove_single_char(s[1:], char_to_remove)
    # Otherwise, include the first character and process the rest of the string.
    else:
        return s[0] + remove_single_char(s[1:], char_to_remove)

def remove_chars_recursive(s, char_to_remove):
    """
    Recursively removes all occurrences of a series of characters from a string.
    Ex: "bcdabcfg" remove abc from string
    Args:
        s (str): The input string.
        char_to_remove (str): The character to be removed.

    Returns:
        str: The new string with all occurrences of char_to_remove removed.
    """
    # Base Case: If the string is empty, return an empty string.
    if not s:
        return ""

    # Recursive Step:
    # If the string starts with is the chars to be removed, skip it.
    if s.startswith(char_to_remove):
        return remove_chars_recursive(s[5:], char_to_remove)
    # Otherwise, include the first character and process the rest of the string.
    else:
        return s[0] + remove_chars_recursive(s[1:], char_to_remove)


def removeAppNotApple(s, chars_to_remove):
    """
    Recursively removes all occurrences of a series of characters from a string.
    Ex: "bcdapplebcfappg" remove "app" instead of "apple" from string
    Args:
        s (str): The input string.
        chars_to_remove (str): The character to be removed.

    Returns:
        str: The new string with all occurrences of chars_to_remove removed.
    """
    # Base Case: If the string is empty, return an empty string.
    if not s:
        return ""

    # Recursive Step:
    # If the first character is the one to be removed, skip it.
    if s.startswith(chars_to_remove) and not s.startswith("apple"):
        return removeAppNotApple(s[3:], chars_to_remove)
    # Otherwise, include the first character and process the rest of the string.
    else:
        return s[0] + removeAppNotApple(s[1:], chars_to_remove)


def generate_sequence(s, unprocessed):
    if not unprocessed:
        print(s)
        return
    
    generate_sequence(s + unprocessed[0], unprocessed[1:])
    generate_sequence(s, unprocessed[1:])
    
generate_sequence('', 'ABC')
# print(removeAppNotApple("bcdapplefgapplefdcs", "app"))