# 438. Find All Anagrams in a String
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only 
and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


# Sliding Window, Time O(N)
def findAnagrams(s,p):
    res = []
    lst_s, lst_p = [0]*26, [0]*26                   #1# Use list [0,0,…,0] to deal with unicode
    for i in range(len(p)):                         #2# loop through p s to get the representing lst_p, [0,1,1,0,…,1]
        lst_s[ ord(s[i])-ord('a') ] += 1
        lst_p[ ord(p[i])-ord('a') ] += 1
    if lst_s == st_p:                               #3# the beginig characters are the same, append index 0 to result
        res.append(0)
        
    for i in range( 1, len(s)-len(p)+1 ):           #4# loop from 1 to the last len(s)-len(p)+1
        lst_s[ ord(s[i-1])-ord('a') ] -= 1          #5# remove previous character
        lst_s[ ord(s[i+len(p)-1])-ord('a') ] += 1   #6# add the new counting character
        if lst_s == lst_p:                          #7# characters are the same, append index i to result
            res.append(i)
    return res

        
                   

