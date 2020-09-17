# take array of coordinates and find shortest in-order path; taxi-cab metric
def in_order_delivery_path(destinations):
    try:
        start = destinations[0]
        distance = 0
        for i in range(len(destinations) - 1):
            if i < len(destinations) - 1:
                x_change = destinations[i + 1][0] - destinations[1][0]
                y_change = destinations[i + 1][1] - destinations[i][1]
                distance += abs(x_change) + abs(y_change)
            else:
                x_change = start[0] - destinations[1][0]
                y_change = start[1] - destinations[i][1]
                distance += abs(x_change) + abs(y_change)
        return distance
    except:
        return -1


coordinates = [(2, 2), (2, 4), (2, 1), (1, 3)]
print(in_order_delivery_path(coordinates))
