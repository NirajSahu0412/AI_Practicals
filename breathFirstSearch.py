graph = {
            '5' : ['3','7'],
            '3' : ['2','4'],
            '7' : ['8'],
            '2' : [],
            '4' : ['8'],
            '8' : []
        }

visited = []

queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while(queue):
        m = queue.pop(0)
        print(m)

        for nextt in graph[m]:
            if nextt not in visited:
                visited.append(nextt)
                queue.append(nextt)

bfs(visited, graph, '5')
