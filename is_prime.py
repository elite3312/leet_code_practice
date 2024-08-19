import sys
def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2: 
         return False
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             print(k)
             return False
         k += 2
    return True
if __name__=="__main__":
    print(is_prime(int(sys.argv[1])))