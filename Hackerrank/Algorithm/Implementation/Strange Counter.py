def Strange_counter(time):
    sum_run,sum_check=0,0
    index=0
    while sum_run<time:
        sum_check=3*pow(2,index)
        sum_run+=3*pow(2,index)
        index+=1
    if sum_check==time:
        return time-2
    elif sum_check>time:
        return abs((sum_check-2)+(sum_check-time))
    else:
        return abs((sum_check-2)-(time-sum_check))



if __name__=="__main__":
    time=int(input())
    print(Strange_counter(time))