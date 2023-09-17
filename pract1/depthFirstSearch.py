graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}


def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        [dfs(nextt) for nextt in graph[node]]


visited = set()
dfs("5")

# Output:
# 5
# 3
# 2
# 4
# 8
# 7
