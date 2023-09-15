def Absolute_permutation(number,query):
    result=[ i for i in range(1,number+1)]
    if query==0:
        return " ".join(map(str,result))
    else:
        if number%2!=0:
            return -1
        else:
            if number%(2*query)!=0:
                return -1
            else:
                result=[ i for i in range(1,number+1)]
                for num in range(1,number+1,2*query):
                    for j in range(0,query):
                        result[num+j-1],result[num+j-1+query]=result[num+j-1+query],result[num+j-1]
                return " ".join(map(str,result))       

if __name__=="__main__":
    test=int(input())
    while test!=0:
        number,query=map(int,input().split())
        print(Absolute_permutation(number,query))
        test-=1