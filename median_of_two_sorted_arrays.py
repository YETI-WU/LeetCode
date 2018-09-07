# median_of_two_sorted_arrays.py
"""
4. Median of Two Sorted Arrays  
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

# O(log(min(m,n))
def median(A,B):
    m, n = len(A), len(B)  
    if m > n :
        A, B, m, n = B, A, n, m  # set m < n, len(A)<len(B), shorter first, longer second
    if n == 0 : 
        raise ValueError
    
    imin, imax, half_len = 0, m, (m+n+1)//2 # parameters for Binary Search
    while imin <= imax :
        i = (imin + imax) // 2  # i: cut_point of A, initial as half of A
        j = half_len - i        # j: cut_point of B, initial as half of B
        if   i > 0  and  A[i-1] > B[j]  :   # left : i is too big ==> decrease it
            imax = i - 1                        # change imax for binary search 
        elif i < m  and  A[i]   < B[j-1]:   # right : i is too small ==> increase it
            imin = i + 1                        # change imin for binary search
        else:                               # i is perfect
            if   i == 0 :   left_max = B[j-1]   # all element in A is bigger than B
            elif j == 0 :   left_max = A[i-1]   # all element in B is bigger than A
            else:           left_max = max(A[i-1],B[j-1])   # when m+n is odd
            
            if (m + n) % 2 == 1:    # when total element is Odd number
                return left_max
            
            if   i == m : right_min = B[j]  # all element in A is smaller than B
            elif j == n : right_min = A[i]  # all element in B is smaller than A
            else:         right_min = min(A[i],B[i])
                
            retrurn (left_max + right_min) / 2.0    # when m+n is even

""" 
########## Description ##########
initial: cut A and B in the middle
find the ideal cut_point i j for A B

      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

initla:	len(left_part) = len(right_part)
find:   max(left_part) ≤ min(right_part)
==> change imax or imin to alter i and j

When the object i is found, the median is:
m+n is odd  ==> max(A[i−1],B[j−1])
m+n is even ==> ( max(A[i-1], B[j-1]) + min(A[i], B[j]) ) / 2
"""
