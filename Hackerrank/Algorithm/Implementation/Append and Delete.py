def Append_delete(string,change,number):
    if number>=len(string)+len(change):
        return "Yes"
    common_count=0
    for i in range(min(len(string),len(change))):
        if string[i]==change[i]:
            common_count+=1
        else:
            break
    if ((len(string)+len(change)-2*common_count)<=number) and ((len(string)+len(change)-2*common_count)%2==number%2):
        return "Yes"
    else:
        return "No"
        


if __name__=="__main__":
    string=input()
    change=input()
    number=int(input())
    print(Append_delete(string,change,number))