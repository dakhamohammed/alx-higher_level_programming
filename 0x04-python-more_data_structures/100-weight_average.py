#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    _score = 0
    _weight = 0

    for score, weight in my_list:
        _score = _score + score * weight
        _weight = _weight + weight

    return _score / _weight
