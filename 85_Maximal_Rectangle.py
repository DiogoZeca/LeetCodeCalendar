# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        left = [0] * m
        right = [m] * m
        height = [0] * m
        max_area = 0
        for i in range(n):
            cur_left, cur_right = 0, m
            for j in range(m):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(m):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            for j in range(m-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = m
                    cur_right = j
            for j in range(m):
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        return max_area