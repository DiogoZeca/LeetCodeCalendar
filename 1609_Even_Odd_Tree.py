# A binary tree is named Even-Odd if it meets the following conditions:
#     The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
#     For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
#     For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        level = 0
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev and node.val <= prev):
                        return False
                else:
                    if node.val % 2 != 0 or (prev and node.val >= prev):
                        return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True