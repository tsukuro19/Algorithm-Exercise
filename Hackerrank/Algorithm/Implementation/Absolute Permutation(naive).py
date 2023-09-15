def Absolute_permutation(number,query):
    result=[]
    if query==0:
        result=[ i for i in range(1,number+1)]
        return " ".join(map(str,result))
    for num in range(1,number+1):
        if num<=query:
            if num+query>number:
                break
            if num+query in result:
                result.append(num-query)
            else:
                result.append(num+query)
        else:
            if num-query>number:
                break
            if num-query in result:
                if num+query>number:
                    break
                result.append(num+query)
            else:
                result.append(num-query)
    if len(result)!=number:
        return -1
    else:
        return " ".join(map(str,result))


if __name__=="__main__":
    test=int(input())
    while test!=0:
        number,query=map(int,input().split())
        print(Absolute_permutation(number,query))
        test-=1