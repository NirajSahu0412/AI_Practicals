import random


def objectiveFunction(x):
    return -(x - 15 * x + 10)


def hillClimbing(maxIteration=1000, stepSize=0.1):
    currentSolution = random.uniform(0, 6)
    currentValue = objectiveFunction(currentSolution)

    for _ in range(maxIteration):
        newSolution = currentSolution + random.uniform(-stepSize, stepSize)
        if 0 <= newSolution <= 6:
            newValue = objectiveFunction(newSolution)
            if newValue > currentValue:
                currentSolution, currentValue = newSolution, newValue

    return currentSolution, currentValue


bestSolution, bestValue = hillClimbing()
print(bestSolution)
print(bestValue)

# Output:
# 5.999896473535772
# 73.99855062950081
