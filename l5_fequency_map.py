# Store frequency of occurance of a numbrs in a list in a dictionary.

freq_dict = {};
hash_map = {};

def freq_map(arr):

    for i in range(0, len(arr)):
        if arr[i] not in freq_dict:
            freq_dict[arr[i]] = 1;
        else:
            freq_dict[arr[i]] += 1;

    print(freq_dict);

freq_map([1, 2, 4, 3, 1, 3, 6, 2, 8, 4]);




# Better way of writing same logic but with simpler code.


def simple_freq_map(arr):
   
    for i in range(0, len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1;
    print(hash_map);


simple_freq_map([1, 2, 4, 3, 1, 3, 6, 2, 8, 4]);
