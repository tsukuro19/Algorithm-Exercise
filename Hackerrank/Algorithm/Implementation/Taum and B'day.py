def Minimum_cost(white,black,white_cost,black_cost,z):
    if white_cost==black_cost:
        return black*black_cost+white*white_cost
    elif black_cost>white_cost:
        if z>black_cost:
            return black*black_cost+white*white_cost
        else:
            if (black+white)*white_cost+black*z>black*black_cost+white*white_cost:
                return black*black_cost+white*white_cost
            else:
                return (black+white)*white_cost+black*z
    else:
        if z>white_cost:
            return black*black_cost+white*white_cost
        else:
            if (black+white)*black_cost+white*z>black*black_cost+white*white_cost:
                return black*black_cost+white*white_cost
            else:
                return (black+white)*black_cost+white*z


if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        white,black=map(int,input().split())
        white_cost,black_cost,z=map(int,input().split())
        print(Minimum_cost(white,black,white_cost,black_cost,z))