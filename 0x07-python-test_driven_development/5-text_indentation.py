#!/usr/bin/python3
"""
This module handles text indentation
"""


def text_indentation(text):
    """
    writes text with two new line after . or ! or ?
    :param text: input string
    :return: None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ind in range(len(text)):
        if text[ind] in '.?:':
            print(text[ind])
            print()
            continue
        if text[ind - 1] in '.?:' and ind != 0:
            continue
        print(text[ind], end="")
