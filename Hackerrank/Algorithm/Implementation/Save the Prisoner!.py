def Save_prison(prisoners,sweets,start_chair):
    candy_remain=((start_chair+sweets)-1)%prisoners
    if candy_remain==0:
        return prisoners
    return candy_remain
    



if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        prisoners,sweets,start_chair=map(int,input().split())
        print(Save_prison(prisoners,sweets,start_chair))