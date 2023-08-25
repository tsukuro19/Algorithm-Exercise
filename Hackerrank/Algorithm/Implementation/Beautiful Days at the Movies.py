def Count_beautiful(start_day,end_day,k):
    days=[i for i in range(start_day,end_day+1)]
    count=0
    for i in range(len(days)):
        days_string=str(days[i])
        if (days[i]-int(days_string[::-1]))%k==0:
            count+=1
    return count

if __name__=="__main__":
    start_day,end_day,k=map(int,input().split())
    print(Count_beautiful(start_day,end_day,k))