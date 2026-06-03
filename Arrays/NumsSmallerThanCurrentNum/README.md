# Intuition
The key insight is that if we sort the array, the position of an element in the sorted array tells us exactly how many elements are smaller than it.

Think about it this way: when we sort an array in ascending order, the smallest element goes to position 0, the second smallest to position 1, and so on. So if an element ends up at position k in the sorted array, it means there are exactly k elements smaller than it.

For example, with nums = [8, 1, 2, 2, 3], the sorted array would be [1, 2, 2, 3, 8]. The element 8 is at index 4 in the sorted array, which means there are 4 elements smaller than it.

However, we can't just sort the original array and return the indices because we need to maintain the original order of elements in our answer. So we:

Create a sorted copy of the array
For each element in the original array, find where it would be placed in the sorted array
The position where an element would be inserted in a sorted array is exactly the count of elements smaller than it. This is what bisect_left does - it finds the leftmost position where we could insert an element to maintain sorted order. This position equals the number of elements that are strictly less than our target element.

The reason we use bisect_left instead of bisect_right is to handle duplicates correctly. When there are duplicate values, bisect_left gives us the position of the first occurrence, which correctly counts only the elements that are strictly smaller than our target value.