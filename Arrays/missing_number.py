# 268. Missing Number
# Gauss formula n(n + 1) / 2

""" Solution 1 (sorting)
    1) Sort the list (ascending order)
    2) Iterate through the sorted list
        3) Use the index as the expected number and compare to the current number
        4) If there is a mismatch, the index will be the missing number
    4) If every index matches up with the number, return N

    Time: O(NlogN)
    Space: O(1) if sorting in-place, otherwise O(N)
    
    key drawbacks: 
     - modifying original list
     - if we don't modify original list, we need to use O(N) extra space
     - O(NlogN) is not the optimal time complexity
"""

def find_missing_number_sorted(nums):
    n = len(nums)						# Example: [3, 0, 1]    [1, 0, 2]
    nums.sort()                         # answer   --> 2        --> 3 == n
                                        
    for i, num in enumerate(nums):		# index    0  1 *2*     0  1  2  *3*
        if num != i:					# list    [0, 1, 3]    [0, 1, 2]
            return i
    return n
        
""" Solution 2 (Gauss's Formula)

    1) Compute the sum of all elements expect to be present(0 + 1 + 2 + ... + N)
    2) Compute the actual sum of the given input
    3) Return the difference between the expected sum and the actual sum

    Example:
        expected numbers: [a, b, c] --> a + b + c
        input: [a, c] --> a + c
        missing number: (a + b + c) - (a + c) 
                        = a + b + c - a - c 
                        = b
    Time: O(N)
    Space: O(1)
"""       
def find_missing_num_formula(nums):
    n = len(nums) # From 0 to n.
     
    # If 0 not included in array (1 to n)
    # n = len(nums) + 1  # Expected range size

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum
            

""" Solution 3 (XOR bitwise operator)
    1) XOR all numbers from 0 to n (complete expected range)
       len(nums) + 1 to include all expected numbers
       
    2) XOR all numbers in the (input) array
    
	https://www.youtube.com/watch?v=EtVzbeD8zGU
	https://www.youtube.com/watch?v=Y2e5duauDuQ
"""
def find_missing_num_xor(nums):
    res = 0
    
    # XOR all numbers from 0 to n (complete expected range)
    for i in range(len(nums) + 1):
        res ^= i
        
    # XOR all elements present in the array
    for num in nums:
        res ^= num
        
    return res


""" Solution 4: XOR indices and values in one loop
    This technique leverages the commutative and associative properties of the XOR operation.
    Because the order doesn't matter, performing res = (res ^ i) ^ arr[i] is mathematically 
    equivalent to XORing all indices first and then all values. 
    This is frequently used in "Missing Number" problems to identify an element by XORing it 
    with the expected range of indices
""" 
def find_missing_number_optimized(nums):
    res = len(nums)
    # num = 3, i = 0, 1, 2
    # for i, num in enumerate(nums):
    #     res ^= i ^ num
    # return res
    for i in range(res):
        res ^= i ^ nums[i]

    return res

if __name__ == "__main__":
    arr = [3, 0, 1]
    # arr = [1, 2, 4, 5] 
    
    print(find_missing_number_optimized(arr))
   