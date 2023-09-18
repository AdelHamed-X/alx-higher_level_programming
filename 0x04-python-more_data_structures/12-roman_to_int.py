#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    for idx in range(len(roman_string)):
        currentvalue = roman[roman_string[idx]]
        if idx + 1 < len(roman_string):
            nextvalue = roman[roman_string[idx + 1]]
            if currentvalue < nextvalue:
                result -= currentvalue
                continue
            else:
                result += currentvalue
                continue
        result += currentvalue
    return result
