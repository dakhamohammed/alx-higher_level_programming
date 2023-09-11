#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        empty_sentence = 0, 'None'
        return empty_sentence
    str_len = len(sentence), sentence[0]
    return str_len
