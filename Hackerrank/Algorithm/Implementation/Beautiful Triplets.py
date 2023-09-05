def Create_triplets(size,number,target):
    count=0
    for i in range(size-2):
        j=i+1
        k=j+1
        while j<size-1 and number[j]-number[i]<=target:
            if number[j]-number[i]==target:
                while k<size and number[k]-number[j]<=target:
                    if number[k]-number[j]==target:
                        count+=1
                    k+=1
            j+=1
    return count

if __name__=="__main__":
    size,target=map(int,input().split())
    numbers=list(map(int,input().split()))
    print(Create_triplets(size,numbers,target))