from utils.test_driver import test_driver_main

# built-in libraries imports
# from collections import Counter
# from collections import deque 
# endof built-in libraries imports
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        '''
        idea: rolling hash.
        well, since we are only looking at the prefix, so no rolling is required here
        just hash the prefixes
        '''
        # set params for hash algo
        base=101# a larger base tends to avoid collisions better
        mod=10**9+7
        max_root_len=100

        # precompute powers
        powers=[1 for x in range(100)]#we only need to hash words with len at most 100
        for i in range(1,100):
            powers[i]=powers[i-1]*base%mod

        #helper func to get the prefix hash or compute hash
        def genhash_or_check(s:str,check:bool,d:dict,max_root_len:int):
            
            '''
            if not check get the hash for the entire str
            else check for prefix hash from a dict
            '''
            hash=0
            for i,c in enumerate(s):
                if i>=max_root_len:break
                hash=(hash*powers[i]+ord(c))%mod
                if check:
                    if d.get(hash):
                        return d[hash]# we use a list to handle hash collisions, and always look to the first hashed value
            if check:return s
            return hash
        
        # gen hash for root str in dictionary
        d={}
        for i,k in enumerate(dictionary):
           hash=genhash_or_check(dictionary[i],False,d,max_root_len)
           d[hash]=dictionary[i]

        # for each word check for shortest prefix hash
        res=[]
        words=sentence.split(' ')
        for w in words:
            res.append(genhash_or_check(w,True,d,max_root_len))
        return " ".join(res)

        
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
                ["cat","bat","rat"], "the cattle was rattled by the battery"
            ],
            "the cat was rat by the bat"
        ],
        [
            [
                ["a","b","c"],"aadsfasf absbs bbab cadsfafs"
            ],
            "a a b c"
        ],
      
       
        
    ]

    test_driver_main(sol.replaceWords,tests,index)
