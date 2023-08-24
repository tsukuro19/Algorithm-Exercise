def Solution(n):
    return sum(int (i) for i in range(1,n+1))-sum(int (i) for i in input().split())

n=int(input())
print(Solution(n))