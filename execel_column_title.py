# 168. Excel Sheet Column Title  
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
"""

"""
Explain the Rule:
A  1    AA  1x26+ 1   BA  2×26+ 1   ...   ZA  26×26+ 1     AAA  1×26²+1×26+ 1   BAA  
B  2    AB  1x26+ 2   BB  2×26+ 2   ...   ZB  26×26+ 2     AAB  1×26²+1×26+ 2   BAB  
.  .    ..  .......   ..  .......   ...   ..  ........     ...  .............   ...  
.  .    ..  .......   ..  .......   ...   ..  ........     ...  .............   ...
.  .    ..  .......   ..  .......   ...   ..  ........     ...  .............   ...
Z 26    AZ  1x26+26   BZ  2×26+26   ...   ZZ  26×26+26     AAZ  1×26²+1×26+26   BAZ  
  
example: ABCD = A×26³ + B×26² + C×26¹ + D = 1×26³ + 2×26² + 3×26¹ + 4  
  
n%26 method may have problem while dealing with character z:
ZZZZ = Z×26³ + Z×26² + Z×26¹ + Z = 26×26³ + 26×26² + 26×26¹ + 26
use (n-1)%26 instead, range from 0 to 25.

ord('A') = 65
"""


def convertToTitle(n):
    res = ''
    while n > 0:
        res = chr( (n-1)%26 + ord('A') ) + res
        n = (n-1) // 26

    return res

 




