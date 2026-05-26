# check palindrome for numbers

def check_palindrome(n):
    num = n
    reversed_number = 0;
    
    while(num>0):
        digit = num%10;
        num = num // 10;
        reversed_number = reversed_number*10 + digit;

    if(reversed_number == n):
        return "Number is a palindrome";

    return "Number is not a palindrome";  


print(check_palindrome(1231));

