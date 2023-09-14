def Change_list(list_result,start,end,k):
    for index in range(start-1,end):
        list_result[index]+=k
    return list_result


if __name__=="__main__":
    number_quantity,queries=map(int,input().split())
    list_number=[0]*number_quantity
    for i in range(queries):
        start,end,k=map(int,input().split())
        Change_list(list_number,start,end,k)
    print(max(list_number))
    