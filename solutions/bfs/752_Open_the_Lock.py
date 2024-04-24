from utils.test_driver import test_driver

from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # Map the next slot digit for each current slot digit.
        next_slot = {"9": "0"}
        for i in range(0,9):
            next_slot[str(i)]=str(i+1)
        # Map the previous slot digit for each current slot digit.
        prev_slot = {"0": "9"}
        for i in range(1,10):
            prev_slot[str(i)]=str(i-1)
        # Set to store visited and dead-end combinations.
        visited_combinations = set(deadends)
        # Queue to store combinations generated after each turn.
        pending_combinations = deque()

        # Count the number of wheel turns made.
        turns = 0

        # If the starting combination is also a dead-end, 
        # then we can't move from the starting combination.
        if "0000" in visited_combinations :
            return -1

        # Start with the initial combination '0000'.
        pending_combinations.append("0000")
        visited_combinations.add("0000")

        while pending_combinations:
            # Explore all combinations of the current level.
            curr_level_nodes_count = len(pending_combinations)
            for _ in range(curr_level_nodes_count):
                # Get the current combination from the front of the queue.
                current_combination = pending_combinations.popleft()

                # If the current combination matches the target, 
                # return the number of turns/level.
                if current_combination == target:
                    return turns

                # Explore all possible new combinations 
                # by turning each wheel in both directions.
                for wheel in range(4):
                    # Generate the new combination 
                    # by turning the wheel to the next digit.
                    new_combination = list(current_combination)
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                    # If the new combination is not a dead-end and 
                    # was never visited, 
                    # add it to the queue and mark it as visited.
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

                    # Generate the new combination 
                    # by turning the wheel to the previous digit.
                    new_combination = list(current_combination)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                    # If the new combination is not a dead-end and 
                    # is never visited, 
                    # add it to the queue and mark it as visited.
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

            # We will visit next-level combinations.
            turns += 1

        # We never reached the target combination.
        return -1
if __name__ == "__main__":
    s = Solution()

    deadends = ["0201","0101","0102","1212","2002"]
    '''
    "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"
    '''
    target = "0202"
    Output= 6

    deadends1 = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target1 = "8888"
    Output1= -1
    tests = [
        [
            # inputs
            [
               deadends,target
            ],
            # res
            Output
        ],
        [
            # inputs
            [
               deadends1,target1
            ],
            # res
            Output1
        ],
        
    ]
    for input, res in tests:
        test_driver(s.openLock, input[0],input[1],  expected=res)
