# Recursion using parameters: 

#print and given string n times using recursion

def func1(string, number_of_times):
    if(number_of_times > 0):
        print(string);
        func1(string, number_of_times-1);


#print(func1('Raghav', 4));





# Find a factorial of a number using recursion

def factorial(num):
    if num == 0:
        return 1;
    
    return num * factorial(num-1);

#print(factorial(20));






# Reverse an array using recursion

def reverse_array(arr, left=0, right=0):

    if(left == 0 and right == 0):
        right = len(arr) - 1;

    if left == right or left > right:
        return arr;

    #swap
    # temp = arr[left];
    # arr[left] = arr[right];
    # arr[right] = temp;

    # or we can also do
    arr[left], arr[right] = arr[right], arr[left];

    return reverse_array(arr, left+1, right-1);


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

print(reverse_array(arr1));




