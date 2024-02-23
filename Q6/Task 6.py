from collections import deque
from queue import PriorityQueue

heuristic_table = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101}
}


def breadth_first_search(graph, source, target):
    visited = set()
    queue = deque([[source]])
    if source == target:
        return [source]
    while queue:
        vertex = queue.popleft()
        node = vertex[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_vertex = list(vertex)
                new_vertex.append(neighbor)
                queue.append(new_vertex)
                if neighbor == target:
                    return new_vertex
            visited.add(node)
    return None


def uniform_cost_search(graph, source, target):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, [source]))
    while not queue.empty():
        cost, vertex = queue.get()
        node = vertex[-1]
        if node not in visited:
            if node == target:
                return vertex
            visited.add(node)
            neighbors = graph[node]
            for neighbor, weight in neighbors.items():
                if neighbor not in visited:
                    total_cost = cost + weight
                    new_vertex = list(vertex)
                    new_vertex.append(neighbor)
                    queue.put((total_cost, new_vertex))
    return None


def greedy_best_first_search(graph, source, target, heuristic):
    visited = set()
    queue = PriorityQueue()
    queue.put((heuristic[source], [source]))
    while not queue.empty():
        _, path = queue.get()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            if node == target:
                return path
            for neighbor, _ in graph[node].items():
                if neighbor not in visited:
                    queue.put((heuristic[neighbor], path + [neighbor]))
    return None


def iterative_deepening_depth_first_search(graph, source, target):
    depth_limit = 0
    while True:
        stack = [(source, [source])]
        visited = set()
        while stack:
            node, path = stack.pop()
            if node == target:
                return path
            if len(path) <= depth_limit:
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append((neighbor, path + [neighbor]))
        depth_limit += 1


def compute_path_cost(path, graph):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += graph[path[i]][path[i + 1]]
    return total_cost

source = input("Enter Starting Point: ")
destination = input("Enter Destination: ")
if source not in graph or destination not in graph:
    print("Invalid Input")
else:
    bfs = breadth_first_search(graph, source, destination)
    if bfs:
        bfs_cost = compute_path_cost(bfs, graph)
        print("Shortest Path By Breadth First Search: ",bfs)
        print("Cost By Breadth First Search: ",bfs_cost)
    else:
        print("No Path Found")
    ucs = uniform_cost_search(graph, source, destination)
    if ucs:
        ucs_cost = compute_path_cost(ucs,graph)
        print("Shortest Path By Uniform Cost Search: ",ucs)
        print("Cost By Uniform Cost Search: ",ucs_cost)
    else:
        print("No Path Found")
    gbfs = greedy_best_first_search(graph, source, destination, heuristic_table)
    if gbfs:
        gbfs_cost = compute_path_cost(gbfs,graph)
        print("Shortest Path By Greedy Best First Search: ",gbfs)
        print("Cost By Greedy Best First Search: ",gbfs_cost)
    else:
        print("No Path Found")
    iddfs = iterative_deepening_depth_first_search(graph, source, destination)
    if iddfs:
        iddfs_cost = compute_path_cost(iddfs,graph)
        print("Shortest Path By Iterative Depth First Search: ",iddfs)
        print("Cost By Iterative Depth First Search: ",iddfs_cost)
    else:
        print("No Path Found")
    sorted_algorithms = sorted([
        ("Breadth-First Search", bfs_cost),
        ("Uniform Cost Search", ucs_cost),
        ("Greedy Best-First Search", gbfs_cost),
        ("Iterative Deepening Depth-First Search", iddfs_cost)
    ], key=lambda x: x[1])
    print("\nShortest Path Algorithms (Ascending Order):")
    for algorithm, cost in sorted_algorithms:
        print(f"{algorithm}: Cost {cost}")
