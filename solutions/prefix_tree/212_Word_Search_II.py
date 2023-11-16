class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False                             
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
            # adjacent directions
            dirs=[(-1,0),(1,0),(0,-1),(0,1)]
            len_r=len(board)
            len_c=len(board[0])

            # use trie to store words
            t=Trie()
            for w in words:
                t.insert(w)

            def inner(r,c,node:TrieNode,path):
                if node.isEnd:
                    res.add(path)
                    if len(node.children)==0:return True # this path is done

                if len(node.children)>0:
                    for d in dirs:
                        next_r,next_c=r+d[0],c+d[1]
                        if next_r>=0 and next_r<len_r and next_c>=0 and next_c<len_c:
                            next_letter=board[next_r][next_c]
                            if not visited[next_r][next_c] and node.children.get(next_letter):
                                visited[next_r][next_c]=True
                                done=inner(next_r,next_c,node.children[next_letter],path+next_letter)
                                if done:
                                    node.children.pop(next_letter)
                                visited[next_r][next_c]=False
                return len(node.children)==0
            res=set()
            
            for r in range(len_r):
                for c in range(len_c):
                    letter=board[r][c]
                    if t.root.children.get(letter ):
                        visited=[[False for _ in range(len_c)]for _ in range(len_r)]
                        visited[r][c]=True
                        inner(r,c,t.root.children.get(letter ),letter)
            return list(res)
            
from utils.test_driver import test_driver

if __name__ == "__main__":
    
    s=Solution()
    board=[["a","b","c"],
           ["a","e","d"],
           ["a","f","g"]]
    words=["eaafgdcba","eaabcdgfa"]
    Output=["eaabcdgfa","eaafgdcba"]
    test_driver(s.findWords,board,words,expected=Output) 

    board=[["a","b","c","e"],
           ["x","x","c","d"],
           ["x","x","b","a"]]
    words=["abc","abcd"]
    Output=["abc","abcd"]
    test_driver(s.findWords,board,words,expected=Output)  

    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    Output= ["eat","oath"]
    test_driver(s.findWords,board,words,expected=Output)

    board = [["a","b"],["c","d"]] 
    words = ["abcb"]
    Output= []
    test_driver(s.findWords,board,words,expected=Output)

    board =[["o","a","b","n"],
            ["o","t","a","e"],
            ["a","h","k","r"],
            ["a","f","l","v"]]
    words =["oa","oaa"]
    Output=["oa","oaa"]
    test_driver(s.findWords,board,words,expected=Output)

class Solution_tle:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        len_r=len(board)
        len_c=len(board[0])

        def inner(r,c,word_index):
            if r<0 or r>=len_r or c<0 or c>=len_c :return False
            if board[r][c]!=w[word_index]or visited[r][c]:return False

            visited[r][c]=True
            if word_index==word_len-1:return True
 
            for d in dirs:
                if inner(r+d[0],c+d[1],word_index+1):
                    return True
            visited[r][c]=False
            return False
        
        res=[]
        for w in words:
            word_len=len(w)
            
            found_w=False
            for r in range(len_r):
                for c in range(len_c):
                    if board[r][c]==w[0] :
                        
                        visited=[[False for _ in range(len_c)]for _ in range(len_r)]
                        if inner(r,c,0):
                            res.append(w)
                            found_w=True
                            break
                if found_w:break
        return res