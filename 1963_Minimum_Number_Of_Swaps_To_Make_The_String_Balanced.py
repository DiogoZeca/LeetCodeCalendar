# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:

#     It is the empty string, or
#     It can be written as AB, where both A and B are balanced strings, or
#     It can be written as [C], where C is a balanced string.

# You may swap the brackets at any two indices any number of times.

# Return the minimum number of swaps to make s balanced.


class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched_open = 0
        unmatched_close = 0
        
        for char in s:
            if char == '[':
                unmatched_open += 1
            else:  # char == ']'
                if unmatched_open > 0:
                    unmatched_open -= 1
                else:
                    unmatched_close += 1
        
        return (unmatched_open + 1) // 2 