def Check_kaprekar_number(number):
    number_square=str(pow(number,2))
    if len(number_square)==1:
        return False
    else:
        right_number=int(number_square[len(number_square)//2:len(number_square)])
        left_number=int(number_square[0:len(number_square)//2])
        if right_number+left_number==number:
            return True
        else:
            return False

def Range_number_kaprekar(start,end):
    result=[]
    if start==1:
        start+=1
        result.append(1)
    for number in range(start,end+1):
        if Check_kaprekar_number(number)==True:
            result.append(number)
    if result==[]:
        return "INVALID RANGE"
    return " ".join(map(str,result))


if __name__=="__main__":
    start=int(input())
    end=int(input())
    print(Range_number_kaprekar(start,end))