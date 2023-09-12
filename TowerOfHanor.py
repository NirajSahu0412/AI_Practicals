def towerOfHanoi(n, sourcePole, destinationPole, auxiliaryPole):
    if n == 1:
        print("Move disk 1 from pole", sourcePole, "to pole", destinationPole)
        return

    towerOfHanoi(n - 1, sourcePole, auxiliaryPole, destinationPole)
    print("Move disk", n, "from pole", sourcePole, "to pole", destinationPole)
    towerOfHanoi(n - 1, auxiliaryPole, destinationPole, sourcePole)

n = 3
towerOfHanoi(n, 'A', 'C', 'B')
