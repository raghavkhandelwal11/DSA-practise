 
'''
  Prestoring values into some datastructure like list / dict / sets and the fetching it 
'''


n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10];
m = [10 , 11, 1, 9, 5, 67, 2];

''' 
Count that how many time the elements of m are occuring in the n array.

 Constraints

 =>  1 <= n[i] <= 10
 => n can have 10^8 elements
 => m can have 10^8 elements
'''

# solution using brute force
for num in m:
    count = 0;
    for x in n: 
        if x == num:
            count += 1;
    #print(count)


'''
Output: 

1
0
1
0
4
0
2



The brute for solutiuon has: 
time complexity O(m x n)
space complexity O(1)


Now suppose if m has 10^8 elements and n has same number of elements then number of operations would be 10^16 which will throw TLE error. 


If the number of operations is more than 10^8 it will throw TLE eror in python

Let think about an optimal solution

lets make a hash list of length 11 and assign 0 to all values
now run a loop through n and increase the value of hashlist index as your iterate on n values.

Now iterate over m and see the corresponding frequency in hash klist array 

this approach has O(n+m) time complexity
space complexity would be O(11) or O(1) because the length is always contant 

'''

hashList = [0] * 11;

#print(hashList)

for num in n: 
    hashList[num] += 1;

for num in m:
    if num < len(hashList):
        #print(hashList[num]);
        pass;
    else:
        #print(0);
        pass;

'''
Lets solve ranother using using dictionary
'''

s = 'azyuyyzaaaa';
q = ['d', 'a', 'y', 'u'];

#find the frequency of letters in q

freq_1 = {};

for letter in s:
    if letter in freq_1:
        freq_1[letter] += 1;
    else : 
        freq_1[letter] = 1;

for letter in q:
    if letter in freq_1:
        print(freq_1[letter]);
    else:
        print(0);

        










