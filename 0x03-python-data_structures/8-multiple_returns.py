#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0 and sentence[0]:
        return len(sentence), sentence[0]
    else:
        return 0, None


sentence = "aewighsopih"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))