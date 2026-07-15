''' Leetcode 448: Find All Numbers Disappeared in an Array
    Solution 1: Brute force solution
    Time Complexity: O(n) - We traverse the list twice, but it's still linear time.
    Space Complexity: O(n) - We use a set to store the numbers present in the   
'''

def findDisappearedNumbers(nums):
    # Convert nums to a set for O(1) average lookup time
    numbers = set(nums)
    res = []
    
    # Return all numbers in range [1, n] that are NOT in the set
    for i in range(1, len(nums) + 1):
        if i not in numbers:
            res.append(i)
    
    # Pythonic syntax
    # return [i for i in range(1, len(nums) + 1) if i not in numbers]          
    return res
 
      
""" Solution 2: Fast set difference
    - set(range(1, len(nums) + 1)) creates a set of all numbers from 1 to n.
    - set(nums) creates a set of all numbers present in the input array.
    - The subtraction operation finds the difference between these two sets, 
    effectively identifying the missing numbers.
    - Finally, we convert the resulting set back to a list and return it.
    
    Time Complexity: O(n) - We traverse the list twice, but it's still linear time.
    Space Complexity: O(n) - We use a set to store the numbers present in the
"""    

def findDisappearedNumbers2(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))    
    
''' Solution 3: Optimal solution
    - The Range: The problem specifies that elements are strictly in the range [1, n], 
    matching the array's index range [0, n-1] when shifted by 1.
    
    - The Flag: If you encounter the number 4, you look at index 3 (4 - 1) and flip its sign to negative.
    A negative value means "we have seen the number corresponding to this index".
    
    - The Scan: In the final list comprehension, any element that remains positive means 
    its corresponding index + 1 was never seen.
    
    Time Complexity: O(n) - We traverse the list twice, but it's still linear time.
    Space Complexity: O(1) - We use the input array itself for marking presence.
'''

def find_disappeared_numbers(nums):
    # Step 1: Mark presence by negating values at corresponding indices
    for num in nums:
        # Use abs() because the value might have been negated already
        index = abs(num) - 1
        # Negate the value at the index if it's positive
        if nums[index] > 0:
            nums[index] = -nums[index]
            
    # Step 2: Any index with a positive value was never "visited"
    res = []
    
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    
    return res
    # return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    
    print(find_disappeared_numbers(nums))