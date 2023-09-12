capacity = (8, 5, 3)
memory = set()
ans = []

def get_next_state(state, from_jug, to_jug):
    max_from, max_to, _ = capacity
    if state[from_jug] > 0 and state[to_jug] < max_to:
        amount_to_move = min(state[from_jug], max_to - state[to_jug])
        new_state = list(state)
        new_state[from_jug] -= amount_to_move
        new_state[to_jug] += amount_to_move
        return tuple(new_state)
    return None

def getAllStates(state):
    if state[0] == 4 and state[1] == 4:
        ans.append(state)
        return True
    
    if state in memory:
        return False
    
    memory.add(state)

    for from_jug in range(3):
        for to_jug in range(3):
            if from_jug != to_jug:
                new_state = get_next_state(state, from_jug, to_jug)
                if new_state and getAllStates(new_state):
                    ans.append(state)
                    return True

    return False

initialState = (8, 0, 0)
print("Starting Work...\n")
getAllStates(initialState)
ans.reverse()
for i in ans:
    print(i)
