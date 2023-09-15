def Check_grid_search(big,small,row_big,col_big,row_small,col_small):
        found=False
        for row in range(row_big-row_small+1):
            for col in range(col_big-col_small+1):
                flag=True
                for row_index_small in range(row_small):
                    for col_index_small in range(col_small):
                        if big[row+row_index_small][col+col_index_small]!=small[row_index_small][col_index_small]:
                            flag=False
                            break
                    if not flag:
                        break
                if flag:
                    found=True
                    return "YES"
        return "NO"


if __name__=="__main__":
    test=int(input())
    while test!=0:
        big,small=[],[]
        row_big,col_big=map(int,input().split())
        for _ in range(row_big):
            big.append(input())
        row_small,col_small=map(int,input().split())
        for _ in range(row_small):
            small.append(input())
        print(Check_grid_search(big,small,row_big,col_big,row_small,col_small))
        test-=1