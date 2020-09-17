from math import sqrt


# coordinates dict format: {'A' : (x, y), 'B' : (j, k), ...}
def build_weighted_graph(coordinates: dict):
    # initialize empty graph
    graph = {}
    # iterate through elements in coordinate list
    for c_0 in coordinates:
        graph[c_0] = {}
        # find distance between c_0 and all other points
        for c_i in set(filter(lambda x: not x == c_0, coordinates)):
            graph[c_0][c_i] = cartesian_distance(coordinates[c_0], coordinates[c_i])
    return graph


def cartesian_distance(x, y):
    distance = sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
    return distance


def dijkstra(start, end, graph):


points = {
    'A': (0, 0),
    'B': (3, 4),
    'C': (10, 5),
    'D': (0, 5),
    'E': (3, 56),
    'F': (10000, 9999),
    'G': (4, 6),
    'H': (4, 7),
    'I': (30, 300),
    'J': (48, 17)
}
print(cartesian_distance(points['A'], points['B']))
print(build_weighted_graph(points))
