#Created a main function under the __main__ namespace. So whenever the global namespace is called, the main
#function gets invoked
def main():
    print ("\t\tVigener Cipher in python")
    
    descision = getDescision()
    message = getMessage()
    key = getKey()
    
    if (descision[0] == 'd' or descision[0] == 'D'):
        print ("Message Decrypted: ", ConvertMessage(descision, message, key))
    elif (descision[0] == 'e' or descision[0] == 'E'):
        print ("Message Encrypted: ", ConvertMessage(descision, message, key))

#Descision taking function        
def getDescision():
    '''
    # Get the descision of the user.
    # Encrypt the message or Decrypt it.
    '''
    while (True):
        print ("What do you want to do? (Encrypt/Decrypt): ",end='')
        desc = input()
        if (desc in 'encrypt e E decrypt d D'.split()):
            return desc
        else:
            print ("Wrong Input. Please input correctly")
                
#Message input function
def getMessage():
    '''
    # Take message as input
    '''
    print ("Enter a message: ", end='')
    mssg = input()
    return mssg
    
#Key input function
def getKey():
    '''
    # Input the key from the user and check whether the key contains only alphabets or not.
    '''
    flag = 0
    while (True):
        print ("Enter a key string: ", end='')
        key = input()
        for i in key:
            if (not(i.isalpha())):
                print("Key Contains invalid characters. Please insert a correct key")
                flag = 1
                break
            else:
                flag = 0

        if (flag == 0):
            return key

#Convert the message according to the descision provided
def ConvertMessage(descision, message, key):
    '''
    # This function converts the message according to the descision provided by the user and stores it in the final string
    '''
    Final = ''
    keyIndex = 0        #Index of the alphabets from ALPHABETS
    key = key.upper()
    len_key = len(key)
    
    for letter in message:
        num = ALPHABETS.find(letter.upper())
        if (letter.isalpha() and (num != -1)):              #if the given letter is an alphabet
            if (descision[0] == 'e' or descision == 'E'):
                num += ALPHABETS.find(key[keyIndex])
            elif (descision[0] == 'd' or descision == 'D'):
                num -= ALPHABETS.find(key[keyIndex])
        
            num = num % 26                                  #Wrap the key around
        
            if (letter.isupper()):
                Final = Final + str(ALPHABETS[num])
            elif (letter.islower()):
                Final = Final + str(ALPHABETS[num].lower())
            
            keyIndex = keyIndex + 1
            if (keyIndex >= len_key):                       #if the Index value exceeds the given key length, reset it
                keyIndex = 0
                
        else:
            Final = Final + letter
    
    return Final
    
ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#calling the main function from the __main__ namespace
if (__name__ == '__main__'):
    main()
