# Python3 implementation to find the count
# of natural numbers up to N digits
 
from math import pow
 
# Function to return the count of
# natural numbers upto N digits
def count(N, B):
    sum = 0
 
    # Loop to iterate from 1 to N
    # and calculating number of
    # natural numbers for every 'i'th digit.
    for i in range(1, N+1):
        sum += (B - 1) * pow(B, i - 1)
    return sum
 
# Driver Code
if __name__ == '__main__':
    N = 2
    B = 10
    print(int(count(N, B)))
