def Encrypted_string(string_encrypt,row,col):
    string_matrix=[]
    temp=0
    for i in range(row):
        if temp+col<len(string_encrypt):
            string_matrix.append(string_encrypt[temp:temp+col])
            temp+=col
        else:
            string_matrix.append(string_encrypt[temp:len(string_encrypt)])
    return string_matrix


if __name__=="__main__":
    string_encrypted=input()
    string_remove_space=string_encrypted.replace(" ","")
    sqrt_length=len(string_remove_space)**.5
    row,col=0,0
    if sqrt_length==int(sqrt_length):
        row=col=int(sqrt_length)
    else:
        row,col=int(sqrt_length),int(sqrt_length)+1
        if row*col<len(string_remove_space):
            row+=1
    result=Encrypted_string(string_remove_space,row,col)
    for i in range(col):
        result_string=""
        for j in range(row):
            if len(result[j])>i:
                result_string+=result[j][i]
        print(result_string,end=" ")

