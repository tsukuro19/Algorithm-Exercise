def Two_Knight(n):
    global total_combination,total_attack
    for i in range(1,n+1):
        total_combination=(pow(i,4)-pow(i,2))/2
        total_attack=4*(i-1)*(i-2)
        print(int(total_combination-total_attack))

n=int(input())
Two_Knight(n)