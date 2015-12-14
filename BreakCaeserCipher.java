/*
 *
 * Caeser Cipher Breaker
 *
 * This code breaks the caeser cipher easily using the brute force technique as only 26 possible combination exist in the
 * english language. And thus it is easy to crack
*/

//Import the scanner class
import java.util.Scanner;

class BreakCaeserCipher
{
    public static void main(String ar[])
    {
        Scanner obj = new Scanner(System.in);
        String str;                             //string for input
        int i, j, ch;

        System.out.print("Enter the message that you want to crack with caeser cipher: ");
        str = obj.nextLine();                   //Input the string

        for (i = 1; i <= 26; i++)
        {
            System.out.print("k = " + i + " String Value: ");
            for (j = 0; j < str.length(); j++)
            {
                ch = str.charAt(j);                         //get the integer value of the current character
                if (Character.isLetter(ch))                 //is the character a letter ?
                {
                    if (Character.isUpperCase(ch))          //Upper case
                    {
                        if (ch + i > 'Z')                   //out of range from 26 characters
                            System.out.print((char)(ch + i - 26));      //Wrap the string around
                        else
                            System.out.print((char)(ch + i));   //else leave it as it is
                    }
                    else
                    {
                        if (ch + i > 'z')
                            System.out.print((char)(ch + i - 26));
                        else
                            System.out.print((char)(ch + i));
                    }
                }
                else                                        //if the character is not letter print it as it is
                    System.out.print((char)ch);
            }
            System.out.println("");
        }
    }
}
