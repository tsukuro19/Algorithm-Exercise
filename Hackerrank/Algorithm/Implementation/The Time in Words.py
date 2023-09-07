def Time_in_word(hour,minute):
    time = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "quarter", "sixteen", 
            "seventeen", "eighteen", "nineteen", 
            "twenty", "twenty one", "twenty two", 
            "twenty three", "twenty four", 
            "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine",'half']
    
    if minute==0:
        return f"{time[hour]} o' clock"
    elif minute in range(1,10):
        return f"{time[hour]} minute past {time[hour]}"
    elif minute in range(10,31):
        if minute==15:
            return f"{time[minute]} past {time[hour]}"
        elif minute==30:
            return f"{time[minute]} past {time[hour]}"
        return f"{time[minute]} minutes past {time[hour]}"
    else:
        if minute==45:
            return f"{time[60-minute]} to {time[hour+1]}"
        return f"{time[60-minute]} minutes to {time[hour+1]}"
    
if __name__=="__main__":
    hour=int(input())
    minute=int(input())
    print(Time_in_word(hour,minute))