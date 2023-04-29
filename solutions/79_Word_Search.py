import heapq


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        board_dict = dict()  # for recording occurrences
        for r in range(len(board)):
            for c in range(len(board[0])):
                # increment board_dict
                if board_dict.get(board[r][c]) == None:
                    board_dict[board[r][c]] = 0
                board_dict[board[r][c]] += 1

        word_dict = dict()  # for recording occurrences
        for char in word:
            if word_dict.get(char) == None:
                word_dict[char] = 0
            word_dict[char] += 1

        # check when board doesn't have all chars of board_dict
        for char in word_dict:
            if char not in board_dict:
                return False
            if board_dict[char] < word_dict[char]:
                return False

        if len(word) == 1 and word in board_dict:
            return True

        self.board = board
        self.word = word
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r, c, 0, board, word):
                    return True
        return False

    def dfs(self, i, j, k, board, word):
        # Recursion will return False if (i,j) is out of bounds or board[i] [j] != word[k] which is current letter we need
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
                k >= len(word) or word[k] != board[i][j]:
            return False
        # If this statement is true then it means we have reach the last    letter in the word so we can return True
        if k == len(word) - 1:
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            # Since we can't use the same letter twice, I'm changing current    board[i][j] to -1 before traversing further
            tmp = board[i][j]
            board[i][j] = -1

            # If dfs returns True then return True so there will be no  further dfs
            if self.dfs(i + x, j + y, k + 1, board, word):
                return True

            board[i][j] = tmp


def test_driver(s: Solution, input1: any, input2: any, expected: str):
    ans = s.exist(input1, input2)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()
    input1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    input2 = "ABCB"
    expected = "False"
    test_driver(s, input1, input2, expected)

    input1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    input2 = "ABCCED"
    expected = "true"
    test_driver(s, input1, input2, expected)

    input1 = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
        "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
    input2 = "AAAAAAAAAAAAABB"
    expected = "false"
    test_driver(s, input1, input2, expected)

    input1 = [["A", "B"], ["C", "D"]]
    input2 = "AB"
    expected = "true"
    test_driver(s, input1, input2, expected)

    input1 = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
        "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
    input2 = "AAAAAAAAAAAAAAB"
    expected = "false"
    test_driver(s, input1, input2, expected)

    input1 = [["a", "b"], ["c", "d"]]
    input2 = "abcd"
    expected = "false"
    test_driver(s, input1, input2, expected)
