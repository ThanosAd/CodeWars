# Code for 'IP Validation' Kata - 6 Kyu
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006

def is_valid_IP(strng):
    counter = 0
    result = strng.split(".")
    if len(result)==4:
        for number in result:
            if number.isdigit():
                if(number.startswith("0") and len(number)>1)  :
                    return False
                elif int(number)>=0 and int(number)<=255 :
                    counter = counter + 1
            else:
                return False
        if counter==4:
            return True
        else:
            return False
    else:
        return False
