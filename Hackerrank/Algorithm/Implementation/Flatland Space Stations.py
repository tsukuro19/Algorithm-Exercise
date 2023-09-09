def Space_station(city_amount,spaces):
    spaces.sort()
    max_distance=max(0,spaces[0]-0)
    for i in range(1,len(spaces)):
        #This value represents the number of cities between these two space stations.
        distance=(spaces[i]-spaces[i-1])//2
        max_distance=max(max_distance,distance)
    max_distance=max(max_distance,city_amount-1-spaces[-1])
    return max_distance


if __name__=="__main__":
    city_amount,space_amount=map(int,input().split())
    spaces=list(map(int,input().split()))
    print(Space_station(city_amount,spaces))