def set_grid(i,j,char,temp_matrix):
    if (i>=0 and i<row) and (j>=0 and j<col):
        temp_matrix[i][j]=char


def Bomberman_game(matrix_bomb,row,col,time):
    if time%2==0:
        grid=[['O']*col for i in range(row)]
        return grid
    else:
        time/=2
        for _ in range(min(int(time),(int(time)+1)%2+1)):
            temp_grid=[['O']*col for i in range(row)]
            for i in range(row):
                for j in range(col):
                    if matrix_bomb[i][j]=="O":
                        set_grid(i,j,".",temp_grid)
                        set_grid(i-1,j,".",temp_grid)
                        set_grid(i+1,j,".",temp_grid)
                        set_grid(i,j-1,".",temp_grid)
                        set_grid(i,j+1,".",temp_grid)
            matrix_bomb=temp_grid
        return matrix_bomb




if __name__=="__main__":
    row,col,time=map(int,input().split())
    matrix_bomb=[]
    for _ in range(row):
        matrix_bomb.append(input())
    result=Bomberman_game(matrix_bomb,row,col,time)
    for i in range(row):
        print("".join(map(str,result[i])))
    