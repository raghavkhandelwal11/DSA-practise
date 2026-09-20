
# start from the first element compare it to the next element 
# if the element is smmaller than preceding element swap them
# repeat till the last element 
# at the end of every loop you will have greatest element at the last.
#repeat the process till all the elements are placed

nums = [5, 4, 7, 1, 2, 9, 8]

def bubble_sort(arr):

    for i in range(len(arr) - 1):
        for j in range(0, len(arr)-i-1):
            if arr[j+1] < arr[i]:
                arr[j+1], arr[j] = arr[j], arr[j+1];

    print(arr);



bubble_sort(nums);



        
