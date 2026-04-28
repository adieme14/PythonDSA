# Leetcode 448: Find All Numbers Disappeared in an Array

def findDisappearedNumbers(nums):
    numbers = set(nums)
    res = []
    
    for n in range(1, len(nums) + 1):
        if n not in numbers:
            res.append(n)
            
    return res
    
if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    
    print(findDisappearedNumbers(nums))