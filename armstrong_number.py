'''
Armstring number example

153 = 1^3 + 5^3 + 3^3

number that shows this kind of nature is armstrong number.
'''

from math import *;

def armstrong_number(num):
    n = num;
    arm_sum = 0;

    count = int(log10(num) + 1);

    for i in range(count):
        arm_sum += (n%10)**count;
        n = n//10;


    if(arm_sum == num):
        return 'It is an Armstrong Number';

    return 'It is not an Armstrong Number';


print(armstrong_number(1635));
