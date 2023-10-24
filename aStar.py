from simpleai.search import SearchProblem, astar

GOAL = "HELLO WORLD"


class HelloProblem(SearchProblem):
    def actions(self, state):
        return list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ") if len(state) < len(GOAL) else []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        return (
            sum(i for i, char in enumerate(state) if char != GOAL[i])
            + len(GOAL)
            - len(state)
        )


problem = HelloProblem(initial_state="")
result = astar(problem)
print(result.state)
print(result.path())

# Output:
# HELLO WORLD
# ['', 'H', 'HE', 'HEL', 'HELL', 'HELLO', 'HELLO ', 'HELLO W', 'HELLO WO', 'HELLO WOR', 'HELLO WORL', 'HELLO WORLD']
