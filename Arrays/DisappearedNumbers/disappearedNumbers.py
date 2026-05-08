''' Leetcode 448: Find All Numbers Disappeared in an Array
    Solution 1
'''

def findDisappearedNumbers(nums):
    # Convert nums to a set for O(1) average lookup time
    numbers = set(nums)
    res = []
    
    # Return all numbers in range [1, n] that are NOT in the set
    for i in range(1, len(nums) + 1):
        if i not in numbers:
            res.append(i)
            
    return res

    # Pythonic syntax
    # return [i for i in range(1, len(nums) + 1) if i not in numbers]
    
'''
    Solution 2: Optimal solution
'''

def find_disappeared_numbers(nums):
    # Step 1: Mark presence by negating values at corresponding indices
    for num in nums:
        # Use abs() because the value might have been negated already
        index = abs(num) - 1
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