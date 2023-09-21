def Larry_array(number,numbers):
    j=1
    while j<number+1:
        index=j-1
        if numbers[index]==j:
            j+=1
            continue
        else:
            location=numbers.index(j)
            distance=location-index
            if distance==1:
                if index+2>=number:
                    return "NO"
                else:
                    element=numbers.pop(index)
                    numbers.insert(location+1,element)
            elif distance%2==0:
                element=numbers.pop(location)
                numbers.insert(index,element)
            elif distance%2==1:
                if index+2>=number:
                    return "NO"
                element=numbers.pop(location)
                numbers.insert(index+1,element)
                j-=1
        j+=1
    return "YES"



if __name__=="__main__":
    test=int(input())
    while test!=0:
        number=int(input())
        numbers=list(map(int,input().split()))
        print(Larry_array(number,numbers))
        test-=1