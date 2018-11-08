#658. Find K Closest Elements 
"""
Medium  Given a sorted array, two integers k and x, 
find the k closest elements to x in the array. 
The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
1.	The value k is positive and will always be smaller than the length of the sorted array.
2.	Length of the given array is positive and will not exceed 104
3.	Absolute value of elements in the array and x will not exceed 104
"""

# Binary Search
def findClosestElements(arr, k , x):
    lo , hi = 0 , len(arr)-k
    while lo < hi :
        mid = (lo + hi) // 2
        if x - arr[mid] > arr[mid+k] - x :
            lo = mid + 1
        else:
            hi = mid
    return arr[lo:lo+k]

# Time O(logN + k): logN for binary search, k for k element
# Space O(k) for k elements





