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

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
#
# text_indentation("     aDel")
