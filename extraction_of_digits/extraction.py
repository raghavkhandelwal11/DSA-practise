#Extraction of digits


# You will be able to solve questions below
# Count digits
# reverse a number
# check palindrome
# armstrong number

'''
What is extraction of digits?

lets say we have a number n = 5873 and we want every number like 5, 8, 7 and 3. This is called extraction of a digit.

'''

n = 5873;

first_digit = n%10;
second_digit = (n//10)%10;
third_digit = ((n//10)//10)%10
fourth_digit = (((n//10)//10)//10)%10

#print(first_digit, second_digit, third_digit, fourth_digit);




# a better way to extract
num = n;
while(num>0):
    last_digit = num%10;
    print(last_digit);
    num = num//10;






