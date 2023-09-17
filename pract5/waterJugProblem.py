from collections import defaultdict

jug1, jug2, aim = 8, 5, 3
visited = defaultdict(lambda: False)


# Function to print the step with jug names
def print_step(amt1, amt2, move):
    print(f"Jug 1 ({amt1}L), Jug 2 ({amt2}L) - {move}")


def waterJugSolver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print_step(amt1, amt2, "Goal Reached!")
        return True

    if not visited[(amt1, amt2)]:
        print_step(amt1, amt2, "Visiting")
        visited[(amt1, amt2)] = True

        return (
            waterJugSolver(0, amt2)
            or waterJugSolver(amt1, 0)
            or waterJugSolver(jug1, amt2)
            or waterJugSolver(amt1, jug2)
            or waterJugSolver(
                amt1 + min(amt2, (jug1 - amt1)), amt2 - min(amt2, (jug1 - amt1))
            )
            or waterJugSolver(
                amt1 - min(amt1, (jug2 - amt2)), amt2 + min(amt1, (jug2 - amt2))
            )
        )
    else:
        return False


print("Steps:")
waterJugSolver(0, 0)

# Output:
# Steps:
# Jug 1 (0L), Jug 2 (0L) - Visiting
# Jug 1 (8L), Jug 2 (0L) - Visiting
# Jug 1 (8L), Jug 2 (5L) - Visiting
# Jug 1 (0L), Jug 2 (5L) - Visiting
# Jug 1 (5L), Jug 2 (0L) - Visiting
# Jug 1 (5L), Jug 2 (5L) - Visiting
# Jug 1 (8L), Jug 2 (2L) - Visiting
# Jug 1 (0L), Jug 2 (2L) - Visiting
# Jug 1 (2L), Jug 2 (0L) - Visiting
# Jug 1 (2L), Jug 2 (5L) - Visiting
# Jug 1 (7L), Jug 2 (0L) - Visiting
# Jug 1 (7L), Jug 2 (5L) - Visiting
# Jug 1 (8L), Jug 2 (4L) - Visiting
# Jug 1 (0L), Jug 2 (4L) - Visiting
# Jug 1 (4L), Jug 2 (0L) - Visiting
# Jug 1 (4L), Jug 2 (5L) - Visiting
# Jug 1 (8L), Jug 2 (1L) - Visiting
# Jug 1 (0L), Jug 2 (1L) - Visiting
# Jug 1 (1L), Jug 2 (0L) - Visiting
# Jug 1 (1L), Jug 2 (5L) - Visiting
# Jug 1 (6L), Jug 2 (0L) - Visiting
# Jug 1 (6L), Jug 2 (5L) - Visiting
# Jug 1 (8L), Jug 2 (3L) - Visiting
# Jug 1 (0L), Jug 2 (3L) - Goal Reached!
