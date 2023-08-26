def Sequence(numbers):
    result=[]
    x=1
    while len(result)!=len(numbers):
        index_result=numbers.index(x)
        result.append(numbers.index(index_result+1)+1)
        x+=1
    return result



if __name__=="__main__":
    number=int(input())
    numbers=list(map(int,input().split()))
    for i in Sequence(numbers):
        print(i)