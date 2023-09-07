def Dynamic_Array(number,queries):
    dynamic_arr=[[] for _ in range(number)]
    last_answer=0
    ans=[]
    for query in queries:
        w,x,y=query
        if w==1:
            dynamic_arr[(x^last_answer)%number].append(y)
        else:
            index=(x^last_answer)%number
            last_answer=dynamic_arr[index][y%len(dynamic_arr[index])]
            ans.append(last_answer)
    return ans


if __name__=="__main__":
    number,number_queries=map(int,input().split())
    queries=[]
    while number_queries!=0:
        query=list(map(int,input().split()))
        queries.append(query)
        number_queries-=1

    for ans in Dynamic_Array(number,queries):
        print(ans)
    