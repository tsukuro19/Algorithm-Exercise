def left_rotation(numbers,rotation):
    for r in range(rotation):
        temp=numbers[0]
        for i in range(len(numbers)-1):
            numbers[i]=numbers[i+1]
        numbers[len(numbers)-1]=temp
    return " ".join(map(str,numbers))

if __name__=="__main__":
    number,rotation=map(int,input().split())
    numbers=list(map(int,input().split()))
    print(left_rotation(numbers,rotation))