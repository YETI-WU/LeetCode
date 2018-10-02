# 204. Count Primes  
"""
Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

# Time O( sqirt(N) log(logN) ) ~ O(N)
def countPrimes(n):
    if n<2 :  return 0
    primes = [True}* n
    primes[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range( i*i, n, i ):
                primes[j] = False
    return sum(primes)
    
    
    
"""
for i = 2, 3, 4, ..., not exceeding √n:
  if primes[i] is true:
    for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n :
      primes[j] := false
Output: all i such that primes[i] is true.
"""
                
