'''
    This file contains the decryption part of message
'''

#import the necessary files
import sys, ReadFromFile

DEFAULT = 128               #default block size
BYTE_SIZE = 256             #One byte contains 256 values according to ASCII

def GetTextFromBlocks(decryptedBlocks, messageLen, blockSize = DEFAULT):
    message = []
    for blockInt in decryptedBlocks:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if (len(message) + i < messageLen):
                asciiVal = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiVal))

        message.extend(blockMessage)

    return ''.join(message)

def DecryptMessage(encryptedBlocks, messageLen, key, blockSize = DEFAULT):
    decryptedBlocks = []
    n, d = key

    for block in encryptedBlocks:
        decryptedBlocks.append(pow(block, d, n))

    return GetTextFromBlocks(decryptedBlocks, messageLen, blockSize)

def Decrypt(filename, keyFile):
    keySize, n, d = ReadFromFile.ReadFromFile(keyFile)

    try:
        with open(filename, 'r') as data:
            content = data.read()
    except IOError as err:
        print ("File Error: " + str(err))
        sys.exit()

    messageLen, blockSize, encryptedMessage = content.split('_')
    messageLen = int(messageLen)
    blockSize = int(blockSize)

    if keySize < blockSize * 8:
        sys.exit("ERROR: Block Size is %s-bits and key size is %s-bts. The RSA-Cipher requires the block size to be equal to or less than the key size."%(blockSize * 8, keySize))

    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    decryptedContent = DecryptMessage(encryptedBlocks, messageLen, (n, d), blockSize)

    try:
        with open ('decrypted_file.txt', 'w') as data:
            data.write(decryptedContent)
    except IOError as er:
        print ("File Error: " + str(er))
    
    return decryptedContent
