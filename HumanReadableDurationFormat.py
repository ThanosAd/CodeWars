# Code for 'Human readable duration format' Kata - 4 Kyu
# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if seconds == 0:
        return "now"
    years = seconds//31536000
    seconds = seconds%31536000
    
    days = seconds//86400
    seconds = seconds%86400
    
    hours = seconds//3600
    seconds = seconds%3600
    
    minutes = seconds//60
    
    seconds = seconds%60
    
    
    formatF = ["year","day","hour","minute","second"]
    values=[years,days,hours,minutes,seconds]
    final = ""
    if years==0:
        formatF.remove("year")
        values.remove(years)  
    if days==0:
        formatF.remove("day")
        values.remove(days)
    if hours==0:
        formatF.remove("hour")
        values.remove(hours)
    if minutes==0:
        formatF.remove("minute")
        values.remove(minutes)
    if seconds==0:
        formatF.remove("second")
        values.remove(seconds)
    
    if len(values)!=1:
        for element in range(0,len(formatF)-1):
        
            if values[element]>1:
                final = final + str(values[element])+ " "+str(formatF[element]) + "s, "
            else:
                final = final +str(values[element])+  " "+ str(formatF[element]) + ", "
        if values[len(values)-1]>1:
            final = final[:-2]
            final = final + " and " +str(values[len(values)-1]) + " "+ str(formatF[len(values)-1])+ "s"
        else:
            final = final[:-2]
            final = final + " and " +str(values[len(values)-1])  + " " +str(formatF[len(values)-1])
    else :
        if values[0]>1:
            final = final[:-2]
            final = final+str(values[0]) + " "+ str(formatF[0])+ "s"
        else:
            final = final[:-2]
            final = final+str(values[0])  + " " +str(formatF[0])
    
    return final
