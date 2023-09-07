def Sale(price,difference,limit,cost):
    count_game=0
    while cost>=0:
        cost-=price
        if price>limit:
            if price-difference>=limit:
                price-=difference
            else:
                price=limit
        if cost>=0:
            count_game+=1
    return count_game


if __name__=="__main__":
    price,difference,limit,cost=map(int,input().split())
    print(Sale(price,difference,limit,cost))