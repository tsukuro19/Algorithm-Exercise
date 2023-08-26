def Find_digit(number,number_digit):
    count=0
    for i in numbers_digit:
        if i==0:
            continue
        else:
            if number%i==0:
                count+=1
    return count

if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        number=int(input())
        numbers_digit=[int(i) for i in str(number)]
        print(Find_digit(number,numbers_digit))