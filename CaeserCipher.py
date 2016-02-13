def getDecision():
    '''
    # Which operation does the user want to perform
    # Encryption or Decryption of the message
    '''
    while (True):
        print ("Encrypt or Decrypt a message ?: ", end=''),
        decision = input()
        if (decision in 'encrypt e decrypt d E D Encrypt Decrypt'.split()):
            return decision
        else:
            print ("You entered wrong text. Please either enter 'encrypt' or 'e' or 'decrypt' or 'd'")

def getMessage():
    '''
    # Input a message
    '''
    print ("Enter your message: ", end='')
    s = input()
    return s

def getKey():
    '''
    # Get the key for rotation
    '''
    print ("Enter the key: ", end='')
    key = int(input())
    key = key % 26
    return key

def getConvMssg(decision, message, key):
    '''
    # This function takes in the operation the user want to perform
    # a message and as well as a key for conversion
    '''
    if (decision[0] == 'd' or decision[0] == 'D'):
        key = -key
    Output = ''
    
    for letter in message:
        
        #Check whether the current character is alphabet
        if (letter.isalpha()):
            # Calculate the ascii sum of the current letter and the key value
            num = ord(letter) + key
            
            #if the current alphabet is an upper case letter
            if (letter.isupper()):
                
                #if the ascii sum goes above 'Z' or below 'A', wrap the letter
                if (num > ord('Z')):
                    num = num - 26
                elif (num < ord('A')):
                    num = num + 26

            #if the current alphabet is a lower case letter
            elif (letter.islower()):
                
                #if the ascii sum goes above 'z' or below 'a', wrap the letter
                if (num > ord('z')):
                    num = num - 26
                elif (num < ord('a')):
                    num = num + 26

            #Add the letter to the output string
            Output = Output + chr(num)
        else:
            Output = Output + letter

    return Output

#Initialise the data
decision = getDecision()    #What operation is to be performed
message = getMessage()      #Get the message that you want to convert
key = getKey()              #Get the key for the rotation

print ("Your Converted message is: ", getConvMssg(decision, message, key))
