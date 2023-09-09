def Cavity_map(matrix,row_number,col_number):
    result_matrix=[]
    for row in range(row_number):
        result_matrix.append(matrix[row])
    for row in range(1,row_number-1):
        for col in range(col_number):
            if col!=0 and col!=col_number-1:
                if int(matrix[row][col])>int(matrix[row-1][col]) and int(matrix[row][col])>int(matrix[row+1][col]) and int(matrix[row][col])>int(matrix[row][col-1]) and int(matrix[row][col])>int(matrix[row][col+1]):
                    result_matrix[row]=list(result_matrix[row])
                    result_matrix[row][col]="X"
                    result_matrix[row]=''.join(result_matrix[row])
    return result_matrix

if __name__=="__main__":
    row_number=col_number=int(input())
    matrix=[]
    for row in range(row_number):
        rows=input()
        matrix.append(rows)
    result_matrix=Cavity_map(matrix,row_number,col_number)
    for i in range(row_number):
        print("".join(map(str,result_matrix[i])))