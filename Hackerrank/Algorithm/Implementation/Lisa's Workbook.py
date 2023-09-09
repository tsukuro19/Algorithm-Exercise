def Work_Book(chapters,k,number_amount):
    count_chapter,count_result=0,0
    pages=[]
    while count_chapter<number_amount:
        problems=[]
        for problem in range(chapters[count_chapter]):
            if len(problems)==k:
                pages.append(problems)
                problems=[]
            problems.append(problem+1)
        if problems!=[]:
            pages.append(problems)
        count_chapter+=1
    for i in range(len(pages)):
        for j in range(len(pages[i])):
            if pages[i][j]==i+1:
                count_result+=1
    return count_result


if __name__=="__main__":
    number_amount,k=map(int,input().split())
    chapters=list(map(int,input().split()))
    print(Work_Book(chapters,k,number_amount))