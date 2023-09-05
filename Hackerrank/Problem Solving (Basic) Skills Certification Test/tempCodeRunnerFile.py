def Maximum_cost_laptop(size,laptops,legals,daily_count):
    maximum_cost,count=0,0
    laptops_price=[]
    for i in range(size):
        if count==daily_count:
            if maximum_cost<sum(laptops_price):
                maximum_cost=sum(laptops_price)
                count=0
                laptops_price=[]
        else:
            if legals[i]=="legal":
                count+=1
            laptops_price.append(laptops[i])
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