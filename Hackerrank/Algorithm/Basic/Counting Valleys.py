def Counting_Valleys(s):
    current,valley=0,0
    for i in range(len(s)):
        if s[i]=='U':
            current+=1
            if current==0:
                valley+=1
        elif s[i]=='D':
            current-=1
    return valley
            

n=int(input())
s=input()
print(Counting_Valleys(s))