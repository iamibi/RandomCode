def ReadFromFile(keyFile):
    try:
        with open (keyFile, 'r') as data:
            content = data.read()
    except IOError as err:
        print ("File Error: " + str(err))

    keySize, n, hashVal = content.split(',')

    return (int(keySize), int(n), int(hashVal))
