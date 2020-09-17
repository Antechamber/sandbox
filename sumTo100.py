# this module searches for combinations of '+', '-' and '', placed between the numbers 1-9 in order and finds
# expressions which evaluate to exactly 100
from itertools import product

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
arr = ['', '-', '+']
operators_combos = product(arr, repeat=8)


# evaluate expression and check whether it sums to 100
def test_equation(eq: str) -> bool:
    value = eval(eq)
    if value == 100:
        return True
    else:
        return False


# alternate operators and numbers to create every possible combination
combined = []
try:
    for item in operators_combos:
        combined.append([item for sublist in zip(numbers, next(operators_combos)) for item in sublist])
except StopIteration:
    # end of generator operator_combos reached
    pass
# collapse lists into string expressions
combined_strings = []
for item in combined:
    item.append('9')
    combined_strings.append(''.join(item))
# test each string expression and print passing expressions
equals_100 = filter(test_equation, combined_strings)
print(list(equals_100))


