import math
def Drawing_Book(n,p):
    turn_up=math.floor(p/2)
    turn_down=math.floor((n-p)/2)
    if turn_down==0:
        if n==p:
            return turn_down
        elif n>p and n%2==0:
            if n==2 and p==1:
                return turn_down
            return turn_down+1
        elif n>p and n%2!=0:
            return turn_down
    else:
        if turn_down<turn_up:
            return turn_down
        else:
            return turn_up

       
n=int(input())
p=int(input())   
print(Drawing_Book(n,p))