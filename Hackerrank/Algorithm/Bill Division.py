def Bill_Division(k,bill,b_over):
    b_actual=round(((sum(bill)-bill[k])/2))
    if b_actual<b_over:
        print(b_over-b_actual)
    else:
        print('Bon Appetit')

n,k=map(int,input().split(' '))
bill=list(map(int,input().split()))
b_over=int(input())
Bill_Division(k,bill,b_over)
