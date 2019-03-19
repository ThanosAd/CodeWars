def encode(message):
    
    rotations = []
    positionOfReal = 0
    
    for letter in message:
        
        message = message[-1] + message[:-1]
        rotations.append(message)
    
    rotations.sort()
    
    lastColumn = ""
    index = 0
    
    for rc in rotations:
    
        lastColumn = lastColumn + rc[-1]
        
        if rc == message:
            positionOfReal = index
        
        index = index + 1
    
    result = (lastColumn,positionOfReal)
    
    return result

def decode(encodedMessage, positionOfReal):
    
    if len(encodedMessage)==0:
        return ""
    
    listOfEncodedMessage = list(encodedMessage)
    finalList = list(encodedMessage)
    finalList.sort()
   
    for j in range(0,len(encodedMessage)-1):
        for i in range(0,len(encodedMessage)):
           
            finalList[i]=listOfEncodedMessage[i] +finalList[i]
            
        finalList.sort()
    
    return finalList[positionOfReal]
