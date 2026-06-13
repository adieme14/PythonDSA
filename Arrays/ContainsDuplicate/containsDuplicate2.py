""" LeetCode 219 (Contains Duplicate II)
    Solution 1: Brute force algorithm. For each element at index i, 
    compare it with every other element (at index j > i) to identify matches
    Time Complexity: O(n^2) quadratic
    Space Complexity: O(1), As we are not using any extra space
    
    * Why i + k + 1? We only need to check indices within distance k of i.
    For example, if i = 0 and k = 3, then we want to check indices 1, 2, and 3 
    (which are within distance 3 of index 0).
     - If we used i + k, we would only check up to index 2, 
        missing index 3 which is still within distance k.
     - The min(i + k + 1, n) ensures that we do not go beyond the end of the array,
        preventing an IndexError when i + k + 1 exceeds n.

    Example: i = 2, k = 3. Then we want to check j = 3, 4, 5 (which are within distance 3 of index 2).
    Since python's range excludes the endpoint, we use range(3, 6) which checks 3, 4, 5. 
    And i + k + 1 = 2 + 3 + 1 = 6, so we check up to index 5 (inclusive).
    
    * Why min? Suppose:
    nums = [1, 2, 3, 4], n = 4, i = 3, and k = 3. Then i + k + 1 = 3 + 3 + 1 = 7, which exceeds n.
    Without min, range(4,7) would attempt to access indices 4, 5, and 6, which are out of bounds.
    Using min(i + k + 1, n) = min(7, 4) = 4, we get range(4, 4), 
    which correctly results in an empty range and prevents any out-of-bounds access.
    There are no elements after 3.

"""
def containsNearbyDuplicateBf(nums, k):
    n = len(nums)
    
    # Outer loop selects the first element
    for i in range(n):
        # Inner loop checks subsequent elements up to distance k
        # the min(i + k + 1, n) prevents j from going past the end of the array.
        for j in range(i + 1, min(i + k + 1, n)):
            if nums[i] == nums[j]:
                return True
    return False


""" Solution 2: Optimal solution approach (hashmap).
    Time Complexity: O(n) - We traverse the list once.
    Space Complexity: O(n) - We could store all elements in the dictionary.
"""

def containsNearbyDuplicate(nums, k):
    # Dictionary to store the most recent index of each element
        index_map = {} # Value -> Last seen index
      
        # Iterate through the array with index and value
        for current_index, value in enumerate(nums):
            # Check if we've seen this value before and if the distance is within k
            if value in index_map and current_index - index_map[value] <= k:
                # Found a duplicate within distance k
                return True
          
            # Update the dictionary with the current index for this value
            # This overwrites any previous index, keeping only the most recent
            index_map[value] = current_index
      
        # No duplicates found within distance k
        return False


""" Solution 3: Sliding window approach (set).
    Time Complexity: O(n) - We traverse the list once.
    Space Complexity: O(min(n, k)) - The set will hold at most k elements at any time.
"""

def containsNearbyDuplicateSlideWin(nums, k):
    window = set()
    left = 0
    
    for right in range(len(nums)):
        # If the window size exceeds k, shrink it from the left
        if right - left > k:
            window.remove(nums[left])
            left += 1
            
        # If the duplicate is inside the current window, return True
        if nums[right] in window:
            return True
            
        window.add(nums[right])
        
    return False


if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    
    print(containsNearbyDuplicate(nums, k))