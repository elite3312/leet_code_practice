class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        # Search character by character in trie
        def inner(cur_node:TrieNode,cur_char_index:int):
            # check return cond
            if cur_node==None or cur_char_index>=len(word):return False
            # check ans cond
            if cur_char_index==len(word)-1:
                if word[cur_char_index]=='.':
                    for c in cur_node.children:
                        if cur_node.children[c].isEnd:return True
                    return False
                else:
                    if cur_node.children.get(word[cur_char_index]):
                        if cur_node.children[word[cur_char_index]].isEnd:return True
                    return False
            
            # go down 1 level
            if word[cur_char_index]=='.':
                for c in cur_node.children:
                    if inner(cur_node.children[c],cur_char_index+1)==True:return True                    
            else:
                if inner(cur_node.children.get(word[cur_char_index]),cur_char_index+1)==True:return True
            return False
        return inner(self.root,0)
                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=WordDictionary()
    s.addWord('c')
    test_driver(s.search,'c',expected=True)

    s.addWord('ab')
    test_driver(s.search,'ab',expected=True)
    test_driver(s.search,'b',expected=False)
    
    s.addWord('apple')
    test_driver(s.search,'apple',expected=True)

    s.addWord('bad')
    test_driver(s.search,'ba.',expected=True)
    test_driver(s.search,'.ad',expected=True)
# idea: use trie to store word, 
# then use dfs to lookup words
