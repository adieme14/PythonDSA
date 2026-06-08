# Leetcode 217
nums = [1,2,3,2]

# Solution 1: Brute force algorithm. For each element at index i,
# compare it with every other element (at index j > i) to identify matches
# Time Complexity: O(n^2) quadratic
# Space Complexity: O(1), As we are not using any extra space

def contains_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


# Solution 2: 

def contain_duplicate_hashset(nums):
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False
            

# Optimal solution: Set implements hash table (lookup/insertion/deletion) is fast O(1) average.
# The {} Trap: Do not use my_set = {}. 
# In Python, empty curly braces create an empty dictionary, not a set (unless you add values).
# Time complexity: O(n) - Python iterates through the entire list once to create the set.
# Space complexity: O(n) — Creating the set always allocates memory proportional to the number 
# of unique elements. (i.e, for storing elements in a set)

def containDuplicate(arr):
    # if len(arr) == len(set(arr)):
    #     return False
    # else:
    #     return True
    # return len(set(nums)) < len(nums
    return len(arr) != len(set(arr))


print(contain_duplicate_hashset(nums))