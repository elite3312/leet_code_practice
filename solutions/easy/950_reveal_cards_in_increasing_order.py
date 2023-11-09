class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        '''
        def f():
            while(1):
                if (deck is empty):break
                pop top and append it to the 'revealed' list
                if (deck is not empty):move top to the bottom of the deck
                else:break
        the goal is to implement f inverse
        '''

        deck.sort()
        return self.f_inverse(deck)

    def f_inverse(self, revealed_deck: list):
        expected_deck = []
        n=len(revealed_deck)
        while (1):
            if len(expected_deck)==n:break
            
            if len(expected_deck) > 0:
                bottom = expected_deck.pop(-1)
                expected_deck.insert(0, bottom)
            if len(revealed_deck) == 0:
                break
            top = revealed_deck.pop(-1)
            expected_deck.insert(0, top)
        return expected_deck

    def test_f_inverse(self):
        revealed_deck = [2, 3, 5, 7, 11, 13, 17]
        print(s.f_inverse(revealed_deck))
        expected_deck = [2, 13, 3, 11, 5, 17, 7]
        print("expected:", expected_deck)


if __name__ == "__main__":
    s = Solution()

    s.test_f_inverse()
    input1 = [17, 13, 11, 2, 3, 5, 7]

    expected = [2, 13, 3, 11, 5, 17, 7]
    print(s.deckRevealedIncreasing(input1), ' ans=', expected)

    input1 = [1,1000]

    expected = [1,1000]
    print(s.deckRevealedIncreasing(input1), ' ans=', expected)
