import random

def objectiveFunction(x):
    return -(x - 3 * x - 5 * x - 7 + 17)

def hillClimbing(maxIteration = 1000, stepSize = 0.1):
    currentSolution = random.uniform(0,6)
    currentValue = objectiveFunction(currentSolution)
    for _ in range(maxIteration):
        newSolution = currentSolution + random.uniform(-stepSize, stepSize)
        if(0 <= newSolution <= 6):
            newValue = objectiveFunction(newSolution)
            if(newValue > currentValue):
                currentValue = newValue
    return currentSolution, currentValue

if(__name__ == "__main__"):
    maxIteration = 1000
    stepSize = 0.1
    bestSolution, bestValue = hillClimbing(maxIteration, stepSize)
    print(bestSolution)
    print(bestValue)
