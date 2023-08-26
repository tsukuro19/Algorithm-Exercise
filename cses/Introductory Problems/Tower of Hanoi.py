def Tower_hanoi(n,start,aux,end):
    if n==0:
        return
    Tower_hanoi(n-1,start,end,aux)
    print(start, end)
    Tower_hanoi(n-1,aux,start,end)

if __name__=="__main__":
    n=int(input())
    start,aux,end=1,2,3
    print(2**n-1)
    Tower_hanoi(n,start,aux,end)