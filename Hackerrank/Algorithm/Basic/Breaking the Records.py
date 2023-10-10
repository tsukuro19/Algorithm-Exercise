def Breaking_the_record(scores):
    high,low=scores[0],scores[0]
    count1,count2=0,0
    for i in range(1,len(scores)):
        if scores[i]>high:
            count1+=1
            high=scores[i]
        elif scores[i]<low:
            count2+=1
            low=scores[i]
    print(count1,count2)

n=int(input())
scores=list(map(int,input().split()))
Breaking_the_record(scores)