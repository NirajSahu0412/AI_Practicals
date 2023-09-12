capacity = (8, 5, 3)
x = capacity[0]
y = capacity[1]
z = capacity[2]

memory = {}

ans = []

def getAllStates(state):
    a = state[0]
    b = state[1]
    c = state[2]

    if(a == 4 and b == 4):
        ans.append(state)
        return True
    
    if((a, b, c) in memory):
        return False
    
    memory[(a, b, c)] = 1

    if(a > 0):
        if(a + b <= y):
            if(getAllStates((0, a + b, c))):
                ans.append(state)
                return True            
        else:
            if(getAllStates((a - (y - b), y, c))):
                ans.append(state)
                return True
            
        if(a + c <= z):
            if(getAllStates((0, b, a + c))):
                ans.append(state)
                return True
        else:
            if(getAllStates((a - (z - c), b, z))):
                ans.append(state)
                return True
            
    if(b > 0):
        if(a + b <= x):
            if(getAllStates((a + b, 0, c))):
                ans.append(state)
                return True            
        else:
            if(getAllStates((x, b - (x - a), c))):
                ans.append(state)
                return True
            
        if(b + c <= z):
            if(getAllStates((a, 0, b + c))):
                ans.append(state)
                return True
        else:
            if(getAllStates((a, b - (z - c), z))):
                ans.append(state)
                return True
            
    if(c > 0):
        if(a + c <= x):
            if(getAllStates((a + c, b, 0))):
                ans.append(state)
                return True            
        else:
            if(getAllStates((x, b, c- (x - a)))):
                ans.append(state)
                return True
            
        if(b + c <= y):
            if(getAllStates((a, b + c, 0))):
                ans.append(state)
                return True
        else:
            if(getAllStates((a, y, c - (y - b)))):
                ans.append(state)
                return True
            
    return False

initialState = (8, 0, 0)
print("Starting Work.....\n")
getAllStates(initialState)
ans.reverse()
for i in ans:
    print(i)