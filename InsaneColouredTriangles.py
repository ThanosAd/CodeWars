# Code for 'Insane Coloured Triangles' Kata - 2 Kyu
# https://www.codewars.com/kata/5a331ea7ee1aae8f24000175

def triangle(row):
    
    row = list(row)
    newRow = row
    letters = ['R','G','B']
    powerOfThree = 1
    
    while len(newRow)!=1:
    
        tempNewRow = list()
        
        while powerOfThree<=len(newRow):
            powerOfThree = powerOfThree*3
            
        if powerOfThree>len(newRow):
            powerOfThree = powerOfThree/3
            
        powerOfThree = int(powerOfThree)
        
        if len(newRow)>= powerOfThree+1:
            for x in range(0,len(newRow)-powerOfThree):
                if newRow[x]==newRow[x+powerOfThree]:
                
                    tempNewRow.extend(newRow[x])
                    
                else:
                
                    list_to_remove=[newRow[x],newRow[x+powerOfThree]]
                    final_list= list(set(letters).difference(set(list_to_remove)))
                    tempNewRow.extend(final_list[0])       
            newRow = tempNewRow
            
        else :
            for x in range(0,len(newRow)-1):
                if newRow[x]==newRow[x+1]:
                
                    tempNewRow.extend(newRow[x])
                    
                else:
                
                    list_to_remove=[newRow[x],newRow[x+1]]
                    final_list= list(set(letters).difference(set(list_to_remove)))
                    tempNewRow.extend(final_list[0])            
            newRow = tempNewRow
    
    return newRow[0]
