# rotate list by n
def list_permute(this_list, n):
    result = []
    length = len(this_list)
    stop = n + length
    while n < stop:
        if n < length:
            result.append(this_list[n])
            n += 1
        elif n >= length:
            result.append(this_list[n % length])
            n += 1
    return result


# tests
print(list_permute([1, 2, 3, 4, 5, 6], 1))
print(list_permute([1, 2, 3, 4, 5, 6], 2))
print(list_permute([1, 2, 3, 4, 5, 6], 3))
print(list_permute([1, 2, 3, 4, 5, 6], 4))
print(list_permute([1, 2, 3, 4, 5, 6], 5))
print(list_permute([1, 2, 3, 4, 5, 6], 6))
print(list_permute([1, 2, 3, 4, 5, 6], 35))
