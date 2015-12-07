'''

    RSA Key Generation program
    
    Key size is 1024-bits
    The RabinMiller generates relatively very large prime numbers of order 2^keySize
    and the Cryptomath checks for the GCD of keys.
    
'''

#import the necessary files
import random, RabinMiller, Cryptomath

def main():
    print ("RSA Key Genarating...")
    makeKey(1024)       #Key size is 1024-bits

def generateKey(keySize):
    print ("Generating p...")
    p = RabinMiller.generateLargePrime(keySize)         #Generate Very large prime numbers from Rabin Miller Algorithm
    print ("Generating q...")
    q = RabinMiller.generateLargePrime(keySize)         #Generate very large prime numbers from Rabin Miller Algorithm

    n = p * q               #Calculate n
    fi = (p - 1) * (q - 1)  #Calculate fi(n)

    print ("Generating e that is co-prime with n and is less than fi(n)...")
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))        #Generate random range of numbers in range 2^(keysize-1) <= e <= 2^keysize
        if (Cryptomath.gcd(e, fi) == 1):                                #if the gcd of the selected 'e' and fi returns true, break
            break

    print ("Generating d such that [(d * e) % fi = 1]...")
    d = Cryptomath.findModInverse(e, fi)                    #calculate d using mod inverse formula

    publicKey = (n, e)
    privateKey = (n, d)

    print ("Public Key (n, e): ", publicKey)
    print ("Private Key (n, d): ", privateKey)

    return (publicKey, privateKey)

def makeKey(keySize):
    publicKey, privateKey = generateKey(keySize)
    print ("The public key is of length %s and a %s digit number."%(len(str(publicKey[0])), len(str(publicKey[1]))))
    print ("The private key is of length %s and a %s digit number."%(len(str(privateKey[0])), len(str(privateKey[1]))))

if __name__ == '__main__':
    main()
