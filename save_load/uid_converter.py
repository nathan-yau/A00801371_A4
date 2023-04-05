def decoder(save_uid: str) -> str:
    """
    Convert a set of joined Unicode numeric strings to a string.

    :param save_uid: a string
    :return: a converted string from a set of joined unicode numeric string
    >>> decoder("00970098")
    'ab'
    >>> decoder("00970099")
    'ac'
    """
    result = []
    for index in range(0, int(len(save_uid)), 4):
        result.append(chr(int(save_uid[index:index + 4])))
    return ''.join(result)


def encoder(phrase: str):
    """

    :param phrase:
    :return:
    """
    translated_message = []
    for index, letter in enumerate(phrase):
        translated_message.append(str(ord(letter)).zfill(4))
    return ''.join(translated_message)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
