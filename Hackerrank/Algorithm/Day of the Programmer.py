def Check_Leap_Year(year):
    if 1700<=year and year<=1917:
        if year%4==0:
            return True
        return False
    else:
        if (year%400==0) or (year%4==0 and year%100!=0):
           return True
        return False

def Day_Of_Programmer(year):
    day=256
    if Check_Leap_Year(year)==True:
        day-=244
        print('12'+'.'+'09'+'.'+str(year))
    elif year==1918:
        print('26.09.1918')
    else:
        day-=243
        print('13'+'.'+'09'+'.'+str(year))

n=int(input())
Day_Of_Programmer(n)