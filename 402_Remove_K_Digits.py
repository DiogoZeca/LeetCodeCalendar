# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k:
            stack.pop()
            k -= 1
        return "".join(stack).lstrip('0') or "0"


