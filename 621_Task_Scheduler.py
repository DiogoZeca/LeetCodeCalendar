# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. 
# Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: 
#                   identical tasks must be separated by at least n intervals due to cooling time.
# ​Return the minimum number of intervals required to complete all tasks.


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)
            
            
            
            
            

