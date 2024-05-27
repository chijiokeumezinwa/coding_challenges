"""
Bin2Dec

Tier: 1-Beginner

Binary is

the number system all digital computers are based on. Therefore it's important for developers to understand binary, 
or base 2, mathematics. The purpose of Bin2Dec is to provide practice and understanding of how binary calculations.

Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays
 its decimal equivalent.

This challenge requires that the developer implementing it follow these constraints:

    Arrays may not be used to contain the binary digits entered by the user
    Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using a 
    single mathematical function, for example the natural logarithm. It's up to you to figure out which function to use.

User Stories

    User can enter up to 8 binary digits in one input field
    User must be notified if anything other than a 0 or 1 was entered
    User views the results in a single output field containing the decimal (base 10) equivalent of the binary number 
    that was entered

"""

def main():
    print("Please enter a string up to 8 binary digits 0's and 1's")

    #check if the string is made up of all digits 0's and 1's.
    #find its value

    input_str= input("String: ")

    if len(input_str) > 8:
        raise Exception("length of string must be less than 8")
    
    list_num=[]
    for i in range(len(input_str)):
        if input_str[i].isdecimal():
            if input_str[i] == '0' or input_str[i] == '1':
                list_num.append(int(input_str[i]))
            else:
                raise Exception("Input must be a 0 or 1 digit")
        else:
            raise Exception("Input must be a digit")
        
    #list_num will be backwards but no concern!
    #to find decimal value just go off the 

    k = len(input_str) - 1

    dec_val=0
    for j in list_num:
        cu_val= j * (2 ** k)
        dec_val += cu_val
        k-=1
    print(dec_val)

if __name__ == "__main__":
    main()