def left_rotation(numbers,rotation):
    index_numbers,index_ans=0,0
    if rotation<=len(numbers):
        index_numbers=rotation
    else:
        index_numbers=len(numbers)%rotation
    count=0
    ans=[0]*len(numbers)
    while count<len(numbers):
        if index_numbers==len(numbers):
            index_numbers=0
        ans[index_ans]=numbers[index_numbers]
        index_numbers+=1
        index_ans+=1
        count+=1
    return " ".join(map(str,ans))



if __name__=="__main__":
    number,rotation=map(int,input().split())
    numbers=list(map(int,input().split()))
    print(left_rotation(numbers,rotation))