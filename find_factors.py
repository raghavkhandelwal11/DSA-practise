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




print(print_factors(23798323));
print((time.time() - start_time)*1000);