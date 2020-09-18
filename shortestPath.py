from math import sqrt
import matplotlib.pyplot as plotter


def build_dijkstra_graph(intersection_coords, road_distance_dict):
    graph = {}
    # loop through coord combos and create direction weight sub-dictionaries from road_distances
    for start in intersection_coords.keys():
        for end in intersection_coords.keys():
            if (start, end) in road_distance_dict.keys():
                if start not in graph.keys():
                    graph[start] = {}
                graph[start][end] = road_distance_dict[(start, end)]
    return graph


def cartesian_distance(x, y):
    distance = sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
    return distance


def dijkstra(start, end, graph):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    inf = float('inf')
    path = []
    for node in unseen_nodes:
        shortest_distance[node] = inf
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, distance in graph[min_node].items():
            if distance + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = distance + shortest_distance[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)

    current_node = end
    while not current_node == start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except:
            print("Path not found")
            break
    path.insert(0, start)
    return 'The shortest distance from %s to %s is :' % (start, end) + '\nBest route: %s' % list(path)


def graph_this_stuff(start, end):
    # plotting points
    for point in intersections.keys():
        plotter.plot(intersections[point][0], intersections[point][1], 'ko')
        plotter.text(intersections[point][0] + 1, intersections[point][1], point, fontsize=15, c='b')
    # plotting roads
    for road in roads.keys():
        plotter.plot((intersections[road[0]][0], intersections[road[1]][0]),
                     (intersections[road[0]][1], intersections[road[1]][1]))
        plotter.text((intersections[road[0]][0] + intersections[road[1]][0]) / 2,
                     (intersections[road[0]][1] + intersections[road[1]][1]) / 2, road_distances[road])

    plotter.ylabel('LAT.')
    plotter.xlabel('LONG.')
    plotter.text(30, 90, dijkstra(start, end, build_dijkstra_graph(intersections, road_distances)), wrap=True)
    plotter.show()


# Map Data:
intersections = {
    'A': (0, 0),
    'B': (15, 4),
    'C': (10, 20),
    'D': (28, 64),
    'E': (70, 56),
    'F': (100, 99),
    'G': (4.7, 59),
    'H': (4, 7),
    'I': (30, 30),
    'J': (48, 17),
    'K': (5, 100)
}
roads = {
    ('A', 'H'): '',
    ('H', 'A'): '',

    ('A', 'B'): '',
    ('B', 'A'): '',

    ('B', 'C'): '',
    ('C', 'B'): '',

    ('B', 'J'): '',
    ('J', 'B'): '',

    ('C', 'I'): '',
    ('I', 'C'): '',

    ('C', 'D'): '',
    ('D', 'C'): '',

    ('D', 'G'): '',
    ('G', 'D'): '',

    ('H', 'G'): '',
    ('G', 'H'): '',

    ('D', 'E'): '',
    ('E', 'D'): '',

    ('I', 'E'): '',
    ('E', 'I'): '',

    ('J', 'E'): '',
    ('E', 'J'): '',

    ('E', 'F'): '',
    ('F', 'E'): '',

    ('H', 'C'): '',
    ('C', 'H'): '',

    ('I', 'G'): '',
    ('G', 'I'): '',

    ('I', 'J'): '',
    ('J', 'I'): '',

}
road_distances = \
    {road: round(cartesian_distance(intersections[road[0]], intersections[road[1]]), 2) for road in roads.keys()}
my_graph = build_dijkstra_graph(intersections, road_distances)

# find shortest path between intersections 'X' and 'Y'
graph_this_stuff('F', 'H')
