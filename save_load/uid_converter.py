def decoder(save_uid: str) -> str:
    """
    Convert a string of joined Unicode numeric strings into an equivalent Unicode character string

    :param save_uid: a string with a length that is a multiple of four
    :precondition: phrase must be a string that is the length of multipler of four
    :postcondition: convert a string of joined Unicode numeric strings to a string of equivalent Unicode characters
    :return: a converted Unicode character string from an equivalent string of joined Unicode numeric strings
    :riase ValueError: if save_uid is not a set of Unicode numeric characters with length of a multiple of four

    >>> decoder("00970098")
    'ab'
    >>> decoder("00970099")
    'ac'
    """
    result = []
    if type(save_uid) is not str or not save_uid.isdigit() or len(save_uid) % 4 != 0:
        raise ValueError("save_uid must be a string of Unicode numeric characters "
                         "with a length that is a multiple of four!")
    for index in range(0, int(len(save_uid)), 4):
        result.append(chr(int(save_uid[index:index + 4])))
    return ''.join(result)


def encoder(phrase: str):
    """
    Convert a Unicode character string into a set of equaivlaent Unicode numeric strings

    :param phrase: a non-empty string that contains Unicode characters with code points less than or equal to 4 digits
    :precondition: phrase must be a non-empty string
    :precondition: phrase must contain Unicode characters with code points less than or equal to 4 digits
    :postcondition: convert a string of Unicode characters into a string of joined Unicode numeric strings
    :return: a set of joined unicode numeric string converted from its unicode character form, which each character is
             represented by exactlt 4 digits
    :raise TypeError: if phrase is not string
    :raise ValueError: if phrase is an empty string

    >>> encoder("{123}")
    '01230049005000510125'
    >>> encoder("[ABC]")
    '00910065006600670093'

    """
    translated_message = []
    if len(phrase) == 0:
        raise ValueError("phrase must not be an empty string!")
    for index, letter in enumerate(phrase):
        translated_message.append(str(ord(letter)).zfill(4))
    return ''.join(translated_message)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
