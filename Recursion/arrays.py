def is_sorted(arr, index):
    if len(arr) == 0:
        return True
    
    if index == len(arr) - 1:
        return True
    
    return arr[index] < arr[index + 1] and is_sorted(arr, index + 1)

def linear_search(arr, target, index): 
    if index == len(arr) - 1:
        return False
    
    if(arr[index] == target):
        return True 
    else:
        return linear_search(arr, target, index + 1)
    
def binary_search(arr, target, lowIndex, highIndex):
    
    if lowIndex >= highIndex:
        return -1
    
    midIndex = (lowIndex + highIndex) // 2
    
    if target == arr[midIndex]:
        return midIndex
    
    if target < arr[midIndex]:
        return binary_search(arr, target, lowIndex, midIndex - 1)
    else:
        return binary_search(arr, target, midIndex + 1, highIndex)
    

def find_element(arr, target, index): 
    if index == len(arr):
        return False
    
    return target == arr[index] or find_element(arr, 55, index + 1)

def find_index(arr, target, index): 
    if index == len(arr):
        return -1
    
    if arr[index] == target:
        return index
    else:
        return find_index(arr, target, index + 1)

''' Start from the end of the array to find target '''    
def find_index_last(arr, target, index): 
    if index == -1:
        return -1
    
    if arr[index] == target:
        return index
    else:
        return find_index_last(arr, target, index - 1)
    
def find_all_index(arr, target, index, list=[]): 
    if index == len(arr):
        return list
    
    if arr[index] == target: 
        list.append(index)
    
    return find_all_index(arr, target, index + 1, list)


# This is not optimize as every calls creates a new list object
def find_all_index2(arr, target, index): 
    list = []
    
    if index == len(arr):
        return list
    
    if arr[index] == target: 
        list.append(index)
    
    return find_all_index(arr, target, index + 1, list)

    
if __name__ == "__main__":
    array = [0, 2, 4, 55, 55, 66, 78]
    
    
    print(find_all_index2(array, 55, 0))