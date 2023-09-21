def Digit_queries(number):
    



if __name__=="__main__":
    query=int(input())
    while query<0:
        number=int(input())
        if number<=9:
            print(number)
        else:
            print(Digit_queries(number))
        query-=1