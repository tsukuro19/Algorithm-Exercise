def Array_rotation(rotation,numbers):
    for _ in range(rotation):
        numbers.insert(0,numbers.pop())
    return numbers



if __name__=="__main__":
    number,rotation,queries=map(int,input().split())
    numbers=list(map(int,input().split()))
    numbers_rotation=Array_rotation(rotation,numbers)
    for _ in range(queries):
        index=int(input())
        print(numbers_rotation[index])