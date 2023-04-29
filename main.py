import heapq

class Solution_tle:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        unique_chars=set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                unique_chars.add(board[r][c])
        for c in set(list(word)):
            if c not in unique_chars :return False

        self.board = board
        self.word = word
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.best_first_search(r, c) == True:
                    return True
        return False

    def best_first_search(self, start_r: int, start_c: int):
        frontier = []
        time_stamp=0
        curr_word = self.board[start_r][start_c]
        h_score=self.heuristic(curr_word, self.word)
        frontier.append((1+h_score+time_stamp,
                         {
                        "curr_word": curr_word,
                        "cost": 1,
                        "visited":[(start_r,start_c)] ,
                        "score": h_score
                        }
        ))
        time_stamp+=0.1
        found_ans = False
        while len(frontier) > 0:
            node = frontier.pop()
            node=node[1]
            if node["curr_word"] == self.word:
                found_ans = True
                break
            
            cost = node["cost"]
            curr_word = node["curr_word"]

            # add good neighbors to queue
            actions = []
            r,c=node['visited'][-1]
            if r-1 >= 0 and ((r-1),c) not in node['visited']:
                actions.append((r-1, c))

            if c-1 >= 0 and (r, c-1) not in node['visited']:
                actions.append((r, c-1))

            if r+1 <= len(self.board)-1 and (r+1, c) not in node["visited"]:
                actions.append((r+1, c))

            if c+1 <= len(self.board[0])-1 and (r, c+1) not in node['visited'] :
                actions.append((r, c+1))
            pass
            for action in actions:
                new_word = curr_word+self.board[action[0]][action[1]]
                new_visted=list(node['visited'])
                new_visted.append(action)
                h_score = self.heuristic(new_word, self.word)
                if h_score > 0:
                    heapq.heappush(frontier,
                                   (cost+1+h_score+time_stamp,
                                    {
                                        "curr_word": new_word,
                                        "cost": cost+1,
                                        "visited": new_visted,
                                        "score": h_score
                                    }))
                    time_stamp+=0.1

        if found_ans:
            return True
        else:
            return False

    def heuristic(self, curr_word: str, target_word: str):
        if len(curr_word) > len(target_word):
            return -100

        # count occurences of unique chars in curr_word
        hash_table_curr_word = [0]*200
        for c in curr_word:
            hash_table_curr_word[ord(c)] += 1

        # count occurences of unique chars in curr_word
        hash_table_target_word = [0]*200
        for c in target_word:
            hash_table_target_word[ord(c)] += 1

        # check similarity
        total_chars = len(target_word)
        correct_chars = 0
        for c in set(list(curr_word)):
            if hash_table_target_word[ord(c)] >= hash_table_curr_word[ord(c)]:
                correct_chars += hash_table_curr_word[ord(c)]
            else:
                return -100
        return correct_chars/total_chars

    def test_heuristic(self):
        target_word = 'ABCTTTTCED'
        curr_word = 'DAE'
        # 3/10=0.3
        print("expected heuristic score = %f, output score = %f" %
              (0.3, self.heuristic(curr_word, target_word)))

        target_word = 'ABC'
        curr_word = 'DAE'
        # 0/3=0
        print("expected heuristic score = %f, output score = %f" %
              (-100, self.heuristic(curr_word, target_word)))

        target_word = 'ABC'
        curr_word = 'AAB'

        print("expected heuristic score = %f, output score = %f" %
              (-100, self.heuristic(curr_word, target_word)))

        target_word = 'ABC'
        curr_word = 'AB'

        print("expected heuristic score = %f, output score = %f" %
              (0.66, self.heuristic(curr_word, target_word)))


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        board=[[1,2],
               [3,4]]
        r=len(board)
        c=len(board[0])
        transpose_board=[[0]*r]*c
        for row in range (r):
            for col in range(c):
                transpose_board[col][row]=board[row][col]
        for i in range(len(word)-1):
            curr_word=word[i:i+2]
            curr_word_exists=False
            for w  in board:
                if ''.join(w). find(curr_word)>=0 or \
                    ''.join(w). find(curr_word[::-1])>=0:
                    curr_word_exists=True
                    break
                    
            if curr_word_exists==False:
                for w in transpose_board:
                    if ''.join(w).find(curr_word)>=0 or \
                        ''.join(w). find( curr_word[::-1])>=0:
                        curr_word_exists=True
                        break
            if curr_word_exists==False:return False
        return True
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    ans = s.exist(input1, input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

    input1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    input2 = "ABCCED"
    expected = "true"
    test_driver(s, input1, input2, expected)
    # s.test_heuristic()
    input1 = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    input2 = "AAAAAAAAAAAAABB"
    expected = "false"
    test_driver(s, input1, input2, expected)

    input1 = [["A", "B"], [ "C", "D"]]
    input2 = "AB"
    expected = "true"
    test_driver(s, input1, input2, expected)


    input1 = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    input2 = "AAAAAAAAAAAAAAB"
    expected = "false"
    test_driver(s, input1, input2, expected)


    input1 = [["a", "b"], ["c", "d"]]
    input2 = "abcd"
    expected = "false"
    test_driver(s, input1, input2, expected)


    


    