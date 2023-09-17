graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}


def bfs(graph, start):
    visited, queue = [], [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.append(node)
            queue.extend(graph[node])


bfs(graph, "5")

# Output:
# 5
# 3
# 7
# 2
# 4
# 8
