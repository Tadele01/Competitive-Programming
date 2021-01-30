import heapq
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        min_heap = []
        count = 0
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                count +=1
                continue
            if ladders:
                heapq.heappush(min_heap, diff)
                count +=1
                ladders -= 1
            else:
                if min_heap and min_heap[0] < diff and bricks-min_heap[0] >= 0:
                    bricks -= heapq.heappop(min_heap)
                    count += 1
                    heapq.heappush(min_heap, diff)
                elif bricks - diff >=0:
                    bricks -= diff
                    count +=1
                else:
                    break
        return count