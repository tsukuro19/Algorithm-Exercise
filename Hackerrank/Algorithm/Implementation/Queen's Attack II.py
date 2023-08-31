#https://www.kindsonthegenius.com/queen-attack-ii-simple-solution-hackerrank/
def queensAttack(n, k, r_q, c_q, obstacles):
    # Initialize the count of attackable squares
    count = 0

    # Create a set of obstacles for efficient lookup
    obstacle_set = set((r, c) for r, c in obstacles)

    # Define the eight possible directions for the queen's movements
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Check each direction for possible attackable squares
    for dr, dc in directions:
        row, col = r_q + dr, c_q + dc
        while 1 <= row <= n and 1 <= col <= n and (row, col) not in obstacle_set:
            count += 1
            row += dr
            col += dc

    return count



if __name__=="__main__":
    n,k=map(int,input().split())
    queenX,queenY=map(int,input().split())
    blocks=[]
    for _ in range(k):
        block=tuple(map(int,input().split()))
        blocks.append(block)
    print(queensAttack(n,k,queenX,queenY,blocks))