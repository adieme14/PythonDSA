# Leetcode 217

""" Solution 1: Brute force algorithm. For each element at index i,
    compare it with every other element (at index j > i) to identify matches
    Time Complexity: O(n^2) quadratic
    Space Complexity: O(1), As we are not using any extra space
"""
def contains_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


""" Solution 2 (optimal): Set implements hash table (lookup/insertion/deletion) is fast O(1) average.
    The {} Trap: Do not use my_set = {}. 
    In Python, empty curly braces create an empty dictionary, not a set (unless you add values).
    Time complexity: O(n) - Python iterates through the entire list once to create the set.
    Space complexity: O(n) — Creating the set always allocates memory proportional to the number 
    of unique elements. (i.e, for storing elements in a set)
"""

def contain_duplicate_hashset(nums):
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False
            
""" 3. Concise Solution: Length Comparison
    Time Complexity: O(n) — Python reads the entire list to build the set.
    Space Complexity: O(n) — The new set requires extra memory allocation.
"""

def containDuplicate(arr):
    # if len(arr) == len(set(arr)):
    #     return False
    # else:
    #     return True
    # return len(set(nums)) < len(nums
    return len(arr) != len(set(arr))


""" 4. Space-Optimized Solution: Sorting
    If you cannot use extra memory (O(1) auxiliary space), sort the list first. 
    Sorting groups identical numbers together, meaning you only need to check adjacent positions.
    Time Complexity: O(nlog n) — Timsort (Python's built-in sorting algorithm) dictates the speed.
    Space Complexity: O(1) — Modifies the input array directly without adding extra data structures.
"""

def containsDuplicateSorted(nums):
    nums.sort()  # Sorts the list in-place
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
    
if __name__ == "__main__":
    nums = [1, 3, 4, 1]
    print(containsDuplicateSorted(nums))