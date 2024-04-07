# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
#     Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack and star:
            if stack[-1] > star[-1]:
                return False
            stack.pop()
            star.pop()
        return not stack


