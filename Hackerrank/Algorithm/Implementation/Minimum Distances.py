def Search_location(numbers,target):
    location=[i for i in range(len(numbers)) if numbers[i]==target]
    if len(location)==2:
        return location[1]-location[0]
    else:
        return -1

def Find_min_distance(numbers,set_number):
    min_result=[]
    for i in range(len(set_number)):
        if Search_location(numbers,set_number[i])==-1:
            continue
        else:
            min_result.append(Search_location(numbers,set_number[i]))
    if min_result==[]:
        return -1
    else:
        return min(min_result)


if __name__=="__main__":
    size=int(input())
    numbers=list(map(int,input().split()))
    set_number=list(set(numbers))
    print(Find_min_distance(numbers,set_number))
