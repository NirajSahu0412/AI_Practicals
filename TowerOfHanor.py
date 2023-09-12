def towerOfHanor(n, sPole, dPole, iPole):
    if(n == 1):
        print("Move disk 1 from pole", sPole, " 2 Pole ", dPole)
        return

    towerOfHanor(n-1, sPole, dPole, iPole)
    print("Move Disk ", n, " From Pole ", sPole, " to Pole ", dPole)

    towerOfHanor(n-1, iPole, dPole, sPole)

n = 10
towerOfHanor(n, 'A', 'C', 'B')
