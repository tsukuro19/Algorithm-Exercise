def Maximum_cost_laptop(size,laptops,legals,daily_count):
    maximum_cost,count,current_cost=0,0,0
    for cost,legal in zip(laptops,legals):
        current_cost+=cost
        if legal=="illegal":
            continue
        count+=1
        if count==daily_count:
            maximum_cost=max(current_cost,maximum_cost)
            current_cost=0
            count=0
    return maximum_cost

if __name__=="__main__":
    number_laptop=int(input())
    laptops=[]
    for i in range(number_laptop):
        laptop=int(input())
        laptops.append(laptop)
    number_legal=int(input())
    legals=[]
    for i in range(number_legal):
        legal=input()
        legals.append(legal)
    daily_count=int(input())
    print(Maximum_cost_laptop(number_laptop,laptops,legals,daily_count))