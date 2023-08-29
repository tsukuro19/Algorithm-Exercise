def Repeat(string,number):
    count_a=string.count('a')
    remain=number%len(string)
    if remain==0:
        return count_a*(number//len(string))
    else:
        remain_string=string[:remain]
        count_a*=(number//len(string))
        count_a+=remain_string.count('a')
        return count_a

if __name__=="__main__":
    string=input()
    number=int(input())
    print(Repeat(string,number))