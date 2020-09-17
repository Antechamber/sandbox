def search(this_list, element):
    def binary_search(list_to_search, x, lower, upper):
        # base case
        if upper >= lower:
            # pick midpoint
            mid = (upper + lower) // 2
            mid_element = list_to_search[mid]
            # if found, return index
            if x == mid_element:
                return mid
            # if x below mid_element, binary search left half of list
            elif x < mid_element:
                return binary_search(list_to_search, x, lower, mid - 1)
            # if x above mid_element, binary search right half of list
            elif x > mid_element:
                return binary_search(list_to_search, x, mid + 1, upper)
        # if x not in list, return -1
        else:
            return -1
    return binary_search(this_list, element, 0, len(this_list) - 1)


# Testing:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 4.5, 1.293, 3.1415926535]
my_list.sort()
print(search(my_list, 7))
print(search(my_list, 2))
print(search(my_list, 98))
