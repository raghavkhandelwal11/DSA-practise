'''
Let say we have a number n = 5873

we want how many digits are there in that number

'''

n = 5873;
num = n;
count = 0;

while(num>0):
    count += 1;
    num = num//10

print(count);


'''
Now what is time and space complexity of above method

    Time complexity
    here because we are doing num//10 in every iteration this means the loop will run for log(n) + 1 times.
    which gives us time complexity of O(log10(n))

    Space Complexity
    we are working with constant space here for space complexity is O(1)

'''

# alternate way is to find the log of n and then add 1 to that result and then do int(result)

from math import *;

def count_digits(num):
    return int(log10(num) + 1);

print(count_digits(5813));

