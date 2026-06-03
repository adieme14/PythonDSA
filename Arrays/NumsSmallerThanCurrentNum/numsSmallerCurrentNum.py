'''
    Solution 1: Brute Force
    Time Complexity: O(N^2)
    Space Complexity: O(N) for the result array
'''
  
def smallerNumbersThanCurrent(arr):
    res = []
    # Loop through each number in the list
    for i in range (len(arr)):
        count = 0
        # Compare current number with every other number
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                count += 1
        res.append(count)
        
    return res


''' Solution 2: Sorting
    Pattern: This problem maps to Counting / Sorting
    Time Complexity: O(N log N) due to sorting
    Space Complexity: O(N) for the sorted array and the result array
'''
def smallerNumbersThanCurrent(arr):
    # Sort the numbers to easily find positions
    # After sorting, the index of each element represents the count of smaller elements
    sorted_nums = sorted(arr)
    #  0  1  2  3  4  -> indices
    # [1, 2, 2, 3, 8]
    
    # Map each unique number to its first index (which is the count of smaller numbers)
    num_to_index = {}
    for i, num in enumerate(sorted_nums):
        if num not in num_to_index:
            num_to_index[num] = i
    
    # Reconstruct the result based on original positions
    res = []        
    for i in nums:
        res.append(num_to_index[i])
    
    return res
        
if __name__ == "__main__":
    nums = [8,1,2,2,3]
    
    print(smallerNumbersThanCurrent(nums))
    