def Space_station(city_amount,spaces):
    result=[]
    for city in range(city_amount):
        min_city=abs(city-spaces[0])
        for i in range(1,len(spaces)):
            if min_city>abs(spaces[i]-city):
                min_city=abs(spaces[i]-city)
        result.append(min_city)
    return max(result)

if __name__=="__main__":
    city_amount,space_amount=map(int,input().split())
    spaces=list(map(int,input().split()))
    print(Space_station(city_amount,spaces))