def towerOfHanoi(n, sourcePole, destinationPole, auxiliaryPole):
    if n == 1:
        print("Move disk 1 from pole", sourcePole, "to pole", destinationPole)
        return

    towerOfHanoi(n - 1, sourcePole, auxiliaryPole, destinationPole)
    print("Move disk", n, "from pole", sourcePole, "to pole", destinationPole)
    towerOfHanoi(n - 1, auxiliaryPole, destinationPole, sourcePole)


n = 3
towerOfHanoi(n, "A", "C", "B")

# Output:
# Move disk 1 from pole A to pole C
# Move disk 2 from pole A to pole B
# Move disk 1 from pole C to pole B
# Move disk 3 from pole A to pole C
# Move disk 1 from pole B to pole A
# Move disk 2 from pole B to pole C
# Move disk 1 from pole A to pole C
