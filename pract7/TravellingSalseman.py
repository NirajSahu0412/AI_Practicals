from itertools import permutations
from sys import maxsize


def tsp(graph, s):
    V = len(graph)
    vertex = [i for i in range(V) if i != s]
    min_cost = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_cost = 0
        k = s
        for j in i:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][s]
        min_cost = min(min_cost, current_cost)

    return min_cost


graph = [[0, 10, 1, 20], [10, 0, 35, 25], [15, 3, 0, 30], [20, 25, 30, 0]]
s = 0
print(tsp(graph, s))

# Output:
# 49
