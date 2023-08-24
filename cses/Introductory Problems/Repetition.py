n=input().upper()
a=len(n)
count=0
max=0
for i in range(a-1):
    if n[i]==n[i+1]:
        count+=1
        if count>=max:
            max=count
    elif n[i]!=n[i+1]:
        count=0
print(max+1)