from datetime import datetime

class Date_borrow:
    def __init__(self,day,month,year):
        self.day_return=day
        self.month_return=month
        self.year_return=year
    
class Date_limit():
    def __init__(self, day, month, year):
        self.day_limit=day
        self.month_limit=month
        self.year_limit=year
    
    def getDay(self):
        return self.day_limit

    def getMonth(self):
        return self.month_limit

    def getYear(self):
        return self.year_limit

    def reduce_book(self,borrow):
        self.fine=0
        if self.year_limit==borrow.year_return:
            if self.month_limit==borrow.month_return:
                if borrow.day_return>self.day_limit:
                    self.fine+=15*(borrow.day_return-self.day_limit)
            else:
                if borrow.month_return>self.month_limit:
                    self.fine+=500*(borrow.month_return-self.month_limit)
        else:
                if borrow.year_return>self.year_limit:
                    self.fine+=10000
        return abs(self.fine)

if __name__=="__main__":
    day_return,month_return,year_return=map(int,input().split())
    day_limit,month_limit,year_limit=map(int,input().split())
    borrow=Date_borrow(day_return,month_return,year_return)
    limit=Date_limit(day_limit,month_limit,year_limit)
    print(limit.reduce_book(borrow))