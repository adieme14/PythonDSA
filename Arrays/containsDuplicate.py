# Leetcode 217
nums = [1,2,3]

# Brute force algorithm. For each element at index i,
# compare it with every other element (at index j > i) to identify matches
# Time Complexity: O(n^2) quadratic
# Space Complexity: O(1), As we are not using any extra space

def contains_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


# Optimal solution: Set implements hash table (lookup/insertion/deletion) is fast O(1) average.
# The {} Trap: Do not use my_set = {}. 
# In Python, empty curly braces create an empty dictionary, not a set (unless you add values).
# Time complexity: O(n)
# Space complexit: for storing elements in a set

def containDuplicate(arr):
    # if len(arr) == len(set(arr)):
    #     return False
    # else:
    #     return True
    # return len(set(nums)) < len(nums
    return len(arr) != len(set(arr))


print(containDuplicate(nums))