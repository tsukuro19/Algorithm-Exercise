def lexi_biggest(string_lexi):
    start=-1
    for i in range(len(string_lexi)-1):
        if string_lexi[i]<string_lexi[i+1]:
            start=i
    if start==-1:
        return "no answer"
    end=-1
    for j in range(start+1,len(string_lexi)):
        if string_lexi[start]<string_lexi[j]:
            end=j
    string_lexi[start],string_lexi[end]=string_lexi[end],string_lexi[start]
    a=string_lexi[start+1:]
    a_sorted=sorted(a)
    for i in range(start+1,len(string_lexi)):
        string_lexi[i]=a_sorted[i-start-1]
    return "".join(string_lexi)


if __name__=="__main__":
    test=int(input())
    while test!=0:
        string_lexi=list(map(str,input().strip()))
        print(lexi_biggest(string_lexi))
        test-=1