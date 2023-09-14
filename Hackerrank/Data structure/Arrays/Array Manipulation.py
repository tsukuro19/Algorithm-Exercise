def Change_list(list_number,start,end,k):
    # add the value at first index
    # subtract the value at last index + 1
    list_number[start-1]+=k
    list_number[end]-=k

def Max_value(list_result):
    maximum=temp=0
    for number in list_result:
        temp+=number
        maximum=max(temp,maximum)
    return maximum

if __name__=="__main__":
    number_quantity,queries=map(int,input().split())
    list_number=[0]*(number_quantity+1)
    for i in range(queries):
        start,end,k=map(int,input().split())
        Change_list(list_number,start,end,k)
    print(Max_value(list_number))
    