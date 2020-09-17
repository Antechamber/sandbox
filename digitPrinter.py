# convert integer into list of digits in order
from math import log10


def digits(x):
    result = []
    num_of_digits = round(log10(x)) + 1
    i = 1
    while i <= num_of_digits:
        if i == 1:
            result.append(x % 10)
        else:
            result.append(int(((x % 10 ** i) - (x % 10 ** (i - 1))) / (10 ** (i - 1))))
        i += 1
    return result[::-1]


print(digits(3141592627498702945072394752934))
