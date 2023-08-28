import math

def Check_square(start,end):
    count=math.isqrt(end) - math.isqrt(start-1)
    return count


if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        start,end=map(int,input().split())
        print(Check_square(start,end))