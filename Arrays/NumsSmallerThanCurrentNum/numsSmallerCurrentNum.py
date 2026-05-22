'''
    Solution 1: Brute Force
    Time Complexity: O(N^2)
    Space Complexity: O(N) for the result array
'''
  
def smallerNumbersThanCurrent(arr):
    res = []
    
    for i in range (len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                count += 1
        res.append(count)
        
    return res

        
if __name__ == "__main__":
    nums = [8,1,2,2,3]
    
    print(smallerNumbersThanCurrent(nums))
    