graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

colors = ['Blue', 'White']


def is_safe(vertex, color, assigned):
    for neighbour in graph[vertex]:
        if assigned.get(neighbour) == color:
            return False
    return True


def graph_coloring(vertices, assigned):
    if len(assigned) == len(vertices):
        return True

    for vertex in vertices:
        if vertex not in assigned:
            break

    for color in colors:
        if is_safe(vertex, color, assigned):
            assigned[vertex] = color

            if graph_coloring(vertices, assigned):
                return True

            del assigned[vertex]

    return False


vertices = list(graph.keys())
assigned = {}

if graph_coloring(vertices, assigned):
    print("Graph Coloring:")
    for vertex in vertices:
        print(vertex, "->", assigned[vertex])
else:
    print("Coloring not possible")
