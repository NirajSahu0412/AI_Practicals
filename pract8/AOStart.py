# Cost to find the AND and OR path
def calculate_path_cost(H, condition, weight=1):
    cost = {}
    if "AND" in condition:
        AND_nodes = condition["AND"]
        Path_A = " AND ".join(AND_nodes)
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    if "OR" in condition:
        OR_nodes = condition["OR"]
        Path_B = " OR ".join(OR_nodes)
        PathB = min(H[node] + weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost


# Update the cost
def update_cost(H, conditions, weight=1):
    least_cost = {}
    for key, condition in conditions.items():
        print(key, ":", condition, ">>>", calculate_path_cost(H, condition, weight))
        c = calculate_path_cost(H, condition, weight)
        H[key] = min(c.values())
        least_cost[key] = calculate_path_cost(H, condition, weight)
    return least_cost


# Print the shortest path
def shortest_path(start, updated_cost, H):
    path = start
    if start in updated_cost.keys():
        min_cost = min(updated_cost[start].values())
        key = list(updated_cost[start].keys())
        values = list(updated_cost[start].values())
        index = values.index(min_cost)

        # FIND MINIMUM PATH KEY
        next_path = key[index].split()
        # ADD TO PATH FOR OR PATH
        if len(next_path) == 1:
            start = next_path[0]
            path += "<--" + shortest_path(start, updated_cost, H)
        # ADD TO PATH FOR AND PATH
        else:
            path += "<--(" + key[index] + ") "

            start = next_path[0]
            path += "[" + shortest_path(start, updated_cost, H) + " + "

            start = next_path[-1]
            path += shortest_path(start, updated_cost, H) + "]"

    return path


H = {"A": -1, "B": 5, "C": 2, "D": 4, "E": 7, "F": 9, "G": 3, "H": 0, "I": 0, "J": 0}

Conditions = {
    "A": {"OR": ["B"], "AND": ["C", "D"]},
    "B": {"OR": ["E", "F"]},
    "C": {"OR": ["G"], "AND": ["H", "I"]},
    "D": {"OR": ["J"]},
}
# weight
weight = 1
# Updated cost
print("Updated Cost:")
Updated_cost = update_cost(H, Conditions, weight=1)
# print("*" * 75)
print("Shortest Path:\n", shortest_path("A", Updated_cost, H))

# Output:
# Updated Cost:
# A : {'OR': ['B'], 'AND': ['C', 'D']} >>> {'B': 5, 'C AND D': 6}
# B : {'OR': ['E', 'F']} >>> {'E': 6, 'F': 8}
# C : {'OR': ['G'], 'AND': ['H', 'I']} >>> {'G': 3, 'H AND I': 1}
# D : {'OR': ['J']} >>> {'J': 0}
# Shortest Path:
# A<--(C AND D) [H AND I + J]<--(H AND I) [H + I]<--H<--0
