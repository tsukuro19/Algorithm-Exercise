def Grid_Challenge(grid,n):
    for i in range(n):
        if i==(n-1):
            break
        for j in range(len(grid[i])):
            if grid[i][j]>grid[i+1][j]:
                return False
    return True

t=int(input())
for i in range(t):
    n=int(input())
    grid=[]
    for i in range(n):
        x=list(input().strip())
        x.sort()
        grid.append(x)
    if Grid_Challenge(grid,n):
        print('YES')
    else:
        print('NO')

