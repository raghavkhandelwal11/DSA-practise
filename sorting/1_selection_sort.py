
# in a given array find the minimum value element and after first iteration swap that element with first element.
# Now in next iteration repeat the same thing process starting from second element.
# Keep doing the same iteration untill last element is placed.



nums = [5, 7, 8, 4, 1, 6, 9, 2];

def selection_sort(arr):
    
    for i in range(len(arr) - 1):
        l_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[l_ind]:
                l_ind = j
        
        #swap
        arr[i], arr[l_ind] = arr[l_ind], arr[i];

    
    print(arr);

selection_sort(nums);

# time complexity is O(n^2)
