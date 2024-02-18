# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:

#     Each meeting will take place in the unused room with the lowest number.
#     If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
#     When a room becomes unused, meetings that have an earlier original start time should be given the room.

# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.



import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = list(range(n))
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have finished by the start of the current meeting
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                # Assign the free room with the lowest index
                room = heapq.heappop(free_rooms)
            else:
                # Delay the meeting until the earliest room gets free
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start
            
            # Book the room
            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1
        
        # Find the room with the maximum bookings
        max_booked = max(count)
        for i in range(n):
            if count[i] == max_booked:
                return i

