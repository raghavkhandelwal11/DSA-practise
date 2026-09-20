

num = [5, 7, 3, 2, 6, 1, 5];

def reverse_array(left, right, arr): 


    
    if (left >= right): 
        return arr;

    arr[left], arr[right] = arr[right], arr[left]
    return reverse_array(left+1, right-1, arr);

print(reverse_array(0, 6, num));





    

    
        