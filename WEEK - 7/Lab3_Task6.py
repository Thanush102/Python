def TowerOfHanoi(n,Source,Auxillary,Destination):
    if n==1:
        print(f"Disk 1 moved from {Source} to {Destination}")
        return 1
    moves=TowerOfHanoi(n-1,Source,Destination,Auxillary)
    print(f"Disk {n} moved from {Source} to {Destination}")
    moves+=1
    moves+=TowerOfHanoi(n-1,Auxillary,Source,Destination)
    return moves
for n in (3,4):
    print(f"Tower of Hanoi for n = {n}")
    TotalMoves=TowerOfHanoi(n,"A","B","C")
    print(f"Moves taken {TotalMoves};Expected Moves {2**n-1}")

"""
Output:
Tower of Hanoi for n = 3
Disk 1 moved from A to C
Disk 2 moved from A to B
Disk 1 moved from C to B
Disk 3 moved from A to C
Disk 1 moved from B to A
Disk 2 moved from B to C
Disk 1 moved from A to C
Moves taken 7;Expected Moves 7
Tower of Hanoi for n = 4
Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C
Disk 3 moved from A to B
Disk 1 moved from C to A
Disk 2 moved from C to B
Disk 1 moved from A to B
Disk 4 moved from A to C
Disk 1 moved from B to C
Disk 2 moved from B to A
Disk 1 moved from C to A
Disk 3 moved from B to C
Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C
Moves taken 15;Expected Moves 15
"""
