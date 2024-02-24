# You are given an integer n indicating there are n people numbered from 0 to n - 1. 
# You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei.
# A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. 
# This secret is then shared every time a meeting takes place with a person that has the secret.
# More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.


from collections import defaultdict
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        for x,y,t in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))

        heap = [(0,firstPerson)] #time,person
        for nei,time in graph[0]:
            heapq.heappush(heap,(time,nei))
        
        visited = set([0])

        while heap:
            time,person = heapq.heappop(heap)

            if person in visited:
                continue

            visited.add(person)

            for nei,t in graph[person]:
                if t>=time:
                    heapq.heappush(heap,(t,nei))

        return visited
    