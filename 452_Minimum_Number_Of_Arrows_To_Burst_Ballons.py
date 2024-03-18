# There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. 
# You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. 
# A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on the start position
        points.sort(key=lambda x: x[0])

        # Initialize the number of arrows and the end position of the first balloon
        num_arrows = 1
        end_position = points[0][1]

        # Iterate through the rest of the balloons
        for balloon in points[1:]:
            # If the start position of the current balloon is beyond the end position of the previous balloon
            if balloon[0] > end_position: 
                # We need another arrow, so increment the count
                num_arrows += 1  
                # Update the end position to the end of the current balloon
                end_position = balloon[1] 
            else:
                # If the current balloon overlaps with the previous balloon, update the end position to the minimum of the two
                end_position = min(end_position, balloon[1])

        # Return the total number of arrows needed
        return num_arrows




