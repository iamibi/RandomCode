/*
    Choose p = 3 and q = 11
    Compute n = p * q = 3 * 11 = 33
    Compute φ(n) = (p - 1) * (q - 1) = 2 * 10 = 20
    Choose e such that 1 < e < φ(n) and e and n are coprime. Let e = 7
    Compute a value for d such that (d * e) % φ(n) = 1. One solution is d = 3 [(3 * 7) % 20 = 1] (1 < d < fi)
    Public key is (e, n) => (7, 33)
    Private key is (d, n) => (3, 33)
    The encryption of m = 2 is c = 2^7 % 33 = 29
    The decryption of c = 29 is m = 29^3 % 33 = 2
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

long int p = 3, q = 11, n, fi, e, d, encr[100], decr[100], c = EOF, temp[100];

long int calculate_d();

// marks all mutiples of 'a' (greater than 'a' but less than equal to 'n') as 1.
void markMultiples(bool arr[], int a, int n)
{
    int i = 2, num;
    while ((num = i*a) <= n)
    {
        arr[num-1] = 1; // minus 1 because index starts from 0.
        i++;
    }
}
 
// A function to print all prime numbers smaller than n
int CoPrime(int n)
{
    int i;
    // There are no prime numbers smaller than 2
    if (n >= 2)
    {
        // Create an array of size n and initialize all elements as 0
        bool arr[n];
        memset(arr, 0, sizeof(arr));
 
        /* Following property is maintained in the below for loop
           arr[i] == 0 means i + 1 is prime
           arr[i] == 1 means i + 1 is not prime */
        for (i = 1; i < n; i++)
            if (arr[i] == 0)
            {
                //(i+1) is prime, print it and mark its multiples
                if ((i + 1) % n != 0 && (i + 1) < fi)
                    return (i + 1);
                markMultiples(arr, i+1, n);
            }
    }
    return 0;
}

int encrypt(const char *ptr)
{
    long int i, tmp, ch;

    for (i = 0; ptr[i] != '\0'; i++)
        temp[i] = ptr[i];

    temp[i] = temp[i+1] = '\0';
    for (i = 0; temp[i] != '\0'; i++)
    {
        ch = (long int)temp[i];
        tmp = pow(ch, e);
        encr[i] = tmp % n;
    }
    encr[i] = -1;
    printf ("Encrypted message: ");
    for (i = 0; encr[i] != -1; i++)
        printf ("%c", (char)encr[i]);
    printf ("\n");
    return 0;
}

int decrypt()
{
    int i, tmp;

    for (i = 0; encr[i] != -1; i++)
    {
        tmp = pow(encr[i], d);
        decr[i] = tmp % n;
    }
    decr[i] = -1;
    printf ("Decrypted text: ");
    for (i = 0; decr[i] != -1; i++)
        printf ("%c", (char)decr[i]);
    printf ("\n");
    return 0;
}

int main()
{
    int len = 0;
    char str[100];

    printf ("p = %ld, q = %ld\n", p, q);
    n = p * q;
    fi = (p - 1) * (q - 1);
    printf ("n = %ld, fi(n) = %ld\n", n, fi);

    e = 7;
    d = calculate_d();
    printf ("Public Key(e, n): (%ld, %ld)\nPrivate Key(d, n): (%ld, %ld)\n", e, n, d, n);
    printf ("Enter the message: ");
    while ((c = getchar()) != '\n' && c != EOF)
        str[len++] = (char)c;

    str[len] = '\000';
    printf ("Unencrypted message: %s\n", str);

    encrypt(str);
    decrypt();
    return 0;
}

long int calculate_d()
{
    long int i;

    for (i = 2; i < fi; i++)
        if ((i * e) % fi == 1)
            return i;

    return 0;
}
