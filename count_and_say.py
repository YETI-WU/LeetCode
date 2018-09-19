# 38. Count and Say  
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"

 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
 10.   13211311123113112211
From the examples you can see, the (i+1)th sequence is the "count and say" of the ith sequence!
"""

def countAndSay(n):
    s = '1'
    for _ in range(n-1):
        count, letter, temp = 0, s[0], ""
        for l in s:
            if letter = l:
                count += 1
            else:
                temp += str(count) + letter
                letter = l
                count = 1
        temp += str(count) + letter
        s = temp
    return s
    
            
