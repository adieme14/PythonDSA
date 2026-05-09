'''
    Solution 1: Brute Force 
    Time complexity: O(n^2) 
    Space complexity: would be O(1) because we are always returning either 
    an array of two elements or an empty array, basically fixed-size data structures
'''
def two_sum_brute_force(nums, target):
    n = len(nums)
    # Outer loop: iterates through each element except the last one
    for i in range(n):
        # Inner loop: iterates through every element AFTER index i
        for j in range(i + 1, n):
            # Check if the sum of the pair matches the target
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Return empty if no solution is found

"""
    Solution 2: Hash Map (Complement)
    Time complexity: O(n)   
    Space complexity: O(n) because in the worst case, we might store all n elements in the hash map
"""

def two_sum_complement(nums, target):
    # Create a hash map to store the complement and its index   
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        if complement in num_to_index:
            return [num_to_index[complement], i]  # Return indices of the pair
        num_to_index[num] = i  # Store the current number and its index in the map  
    return []  # Return empty if no solution is found 

  
if __name__ == "__main__":
        #  0  1  2   3
    arr = [2, 7, 11, 15]
    target = 9
    
    print(two_sum_complement(arr, target))