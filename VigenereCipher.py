ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print ("\t\tVigener Cipher in python")
    
    descision = getDescision()
    message = getMessage()
    key = getKey()
    
    if (descision[0] == 'd' or descision[0] == 'D'):
        print ("Message Decrypted: ", ConvertMessage(descision, message, key))
    elif (descision[0] == 'e' or descision[0] == 'E'):
        print ("Message Encrypted: ", ConvertMessage(descision, message, key))
        
def getDescision():
    while (True):
        print ("What do you want to do? (Encrypt/Decrypt): ",end='')
        desc = input()
        if (desc in 'encrypt e E decrypt d D'.split()):
            return desc
        else:
            print ("Wrong Input. Please input correctly")
                
def getMessage():
    print ("Enter a message: ", end='')
    mssg = input()
    return mssg
    
def getKey():
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
    
def ConvertMessage(descision, message, key):
    Final = ''
    keyIndex = 0
    key = key.upper()
    len_key = len(key)
    
    for letter in message:
        num = ALPHABETS.find(letter.upper())
        if (letter.isalpha() and (num != -1)):
            if (descision[0] == 'e' or descision == 'E'):
                num += ALPHABETS.find(key[keyIndex])
            elif (descision[0] == 'd' or descision == 'D'):
                num -= ALPHABETS.find(key[keyIndex])
        
            num = num % 26
        
            if (letter.isupper()):
                Final = Final + str(ALPHABETS[num])
            elif (letter.islower()):
                Final = Final + str(ALPHABETS[num].lower())
            
            keyIndex = keyIndex + 1
            if (keyIndex >= len_key):
                keyIndex = 0
                
        else:
            Final = Final + letter
    
    return Final
    
if (__name__ == '__main__'):
    main()
