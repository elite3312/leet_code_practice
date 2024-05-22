from utils.test_driver import test_driver
# not solved, wrong
class Solution:
    # Python program to print all Primes Smaller 
    # than or equal to N using Sieve of Eratosthenes
    def e(self,n):
        l=self.SieveOfEratosthenes(n<<5)
        res=1e7
        for p in l:
            cur=p^n
            res=min(cur,res)
        return res

    def SieveOfEratosthenes(self,num):
        prime = [True for i in range(num+1)]
    # boolean array
        p = 2
        while (p * p <= num):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Updating all multiples of p
                for i in range(p * p, num+1, p):
                    prime[i] = False
            p += 1

        # Print all prime numbers
        l=[]
        for p in range(2, num+1):
            if prime[p]:
                l.append(p)
        return l




if __name__ == "__main__":
    s = Solution()
    index=0

    
    tests = [
        [
            # inputs
            [
               1
            ],
            # res
            0
        ],
        [
            # inputs
            [
               2
            ],
            # res
            0
        ],
       
        
    ]
    for input, res in tests[index:]:
        test_driver(s.e, input[0],   expected=res)
