import random, sys

DEFAULT = 128
BYTE_SIZE = 256

def main():
    print ("RSA ASYMMETRIC CRYPTOGRAPHIC ALGOROTHM")
    mode = input("Enter the mode (Encrypt or Decrypt): ")

    if mode[0] in 'E e'.split():
        filename = 'encryted_file.txt'
        public_key_file = 'key_file_pubkey.txt'

        message = input("Enter the message that you want to encrypt: ")
        print ("Encrypting and writing to the file %s..."%(filename))

        encrypted_message = Encrypt(message, filename, public_key_file)
        print ("Encrypted message: %s"%(encrypted_message))
    else:
        print ("Wrong Choice...Exiting")
        sys.exit()

def GetBlocksFromText(message, blockSize = DEFAULT):
    messageBytes = message.encode('ascii')
    
    blockInteger = []
    for start in range (0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range (start, min(start + blockSize, len(messageBytes))):
            blockInt = blockInt + messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInteger.append(blockInt)

    return blockInteger
    
def ReadFromFile(keyFile):
    try:
        with open (keyFile, 'r') as data:
            content = data.read()
    except IOError as err:
        print ("File Error: " + str(err))

    keySize, n, hashVal = content.split(',')

    return (int(keySize), int(n), int(hashVal))

def EncryptMessage(message, key, blockSize = DEFAULT):
    encrBlock = []
    n, e = key

    for block in GetBlocksFromText(message, blockSize):
        encrBlock.append(pow(block, e, n))

    return encrBlock

def Encrypt(message, filename, keyFile, blockSize = DEFAULT):
    keySize, n, e = ReadFromFile(keyFile)

    if keySize < blockSize * 8:
        sys.exit("ERROR: Block size is %s-bits and key size is %s-bits. RSA cipher requires the block size to be equal to or less than the key size."%(blockSize * 8, keySize))
    
    encrypted_block = EncryptMessage(message, (n, e), blockSize)

    for i in range (len(encrypted_block)):
        encrypted_block[i] = str(encrypted_block[i])

    encrypted_content = ','.join(encrypted_block)
    encrypted_content = '%s_%s_%s'%(len(message), blockSize, encrypted_content)
    
    try:
        with open(filename, 'w') as data:
            data.write(encrypted_content)
    except IOError as err:
        print ("File Error: " + str(err))

    return encrypted_content

if __name__ == '__main__':
    main()
