'''
Find all the factors of the given number

lets first check brute force solution


example take number num = 20

check all numbers with 20%number
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

result = [];
for i in range(1, num+1):
    if(num%i == 0):
        result.append(i);

for this approach the time complexity is O(n) and space complexity is O(K) where K is total number of factors.



Lets now consider a more optimised approach

suppose we have num = 10;

1 2 3 4 5 6 7 8 9 10

there can be no factors between 10/2 and 10. as 2 is the minimum factor which gives 10/2 = 5;

this mean num/2 to num we can skip while applying conditions

given that num = 10


result = [];
for i in range(1, num//2):
    if num%i == 0:
        result.append(i)

'''

import time;

def print_factors(num):
    n = num;
    if(num == 1):
        return [1];
    result = [];
    for i in range(1, n//2 + 1):
        if num%i == 0:
            result.append(i)
    result.append(num);
    return result;
start_time = time.time();


print(print_factors(100000));
print((time.time() - start_time)*1000);





'''

Now there is even more optimised approach:

lets say that number is 36. If 36 is divisible by 2 then we get 36/2 = 18 this means 36 is also divisible by 18. we got 2 factor by doing just one operation.


let try to code this optimised approach and note the time duration to execute this.

'''
import math;


def optimised_prime_factors(num):
    factors = [];
    limit = math.sqrt(num) // 1;
    for i in range(1, int(limit) + 1):
        if(num%i == 0):
            factors.append(i);
            if(i != num/i):
                factors.append(num/i);
    print(factors);
    return factors;


start_time = time.time();
optimised_prime_factors(100000);
print('Time taken: ', (time.time() - start_time)*1000);
