# Solution 1 (Brute Force)

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

   
if __name__ == "__main__":
        #  0  1  2   3
    arr = [2, 7, 11, 15]
    target = 9
    
    print(two_sum_brute_force(arr, target))