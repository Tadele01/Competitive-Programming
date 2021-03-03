from typing import List
class Solution:
    def calculate_area(self, pos1, pos2):
        area = (pos2[0] - pos1[0]) * min(pos1[1], pos2[1])
        return abs(area)
    def maxArea(self, height: List[int]) -> int:
        left, right = (0, height[0]), (len(height)-1, height[-1])
        max_area = self.calculate_area(left, right)
        for i in range(1, len(height)):
            if left[1] > right[1]:
                right = (right[0]-1, height[right[0]-1])
            elif right[1] > left[1]:
                left = (left[0]+1, height[left[0]+1])
            else:
                right = (right[0]-1, height[right[0]-1])
                left = (left[0]+1, height[left[0]+1])
            area = self.calculate_area(left, right)
            max_area = max(area, max_area)
        return max_area