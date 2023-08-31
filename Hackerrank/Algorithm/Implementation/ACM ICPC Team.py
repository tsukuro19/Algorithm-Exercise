def Create_team(topics):
    max_topic=0
    count=0
    for i in range(n):
        for j in range(i+1,n):
            result = bin(int(topics[i], 2) | int(topics[j], 2))[2:]
            if result.count('1')>max_topic:
                max_topic=result.count('1')
                count=1
            elif result.count('1')==max_topic:
                count+=1
    return [max_topic,count]
            


if __name__=="__main__":
    n,m=map(int,input().split())
    topics=[]
    for _ in range(n):
        topic=input()
        topics.append(topic)
    for i in Create_team(topics):
        print(i)