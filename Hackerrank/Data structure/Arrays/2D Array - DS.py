def Sum_hourglass(matrix):
    #each hourglass has 7 element, smallest value is -9==>9*-7
    sum_max=-63
    for i in range(4):
        for j in range(4):
             # sum of top 3 elements
            top=sum(matrix[i][j:j+3])
            #sum of mid
            mid=matrix[i+1][j+1]
            #sum of bottom 3 elements
            bottom=sum(matrix[i+2][j:j+3])
            sum_hourglass=top+mid+bottom
            if sum_max<sum_hourglass:
                sum_max=sum_hourglass
    return sum_max



if __name__=="__main__":
    matrix=[]
    for i in range(6):
        row=list(map(int,input().split()))
        matrix.append(row)
    print(Sum_hourglass(matrix))