#https://www.hackerrank.com/challenges/manasa-and-stones/editorial
def Manasa_and_stones(c,d,number):
    set_stones=set()
    a=min(c,d)
    b=max(c,d)
    for i in range(number):
        set_stones.add(i*b+(number-i-1)*a)
    return " ".join(map(str,sorted(list(set_stones))))



if __name__=="__main__":
    test_case=int(input())
    while test_case!=0:
        number=int(input())
        difference_1=int(input())
        difference_2=int(input())
        print(Manasa_and_stones(difference_1,difference_2,number))
        test_case-=1
