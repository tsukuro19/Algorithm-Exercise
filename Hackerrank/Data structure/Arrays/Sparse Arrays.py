def Sparse_arrays(string_list,query_list):
    ans=[]
    for query in query_list:
        ans.append(string_list.count(query))
    return ans


if __name__=="__main__":
    string_count=int(input())
    string_list,query_list=[],[]
    for _ in range(string_count):
        string_item=input()
        string_list.append(string_item)
    query_count=int(input())
    for _ in range(query_count):
        query_string=input()
        query_list.append(query_string)
    for element in Sparse_arrays(string_list,query_list):
        print(element)