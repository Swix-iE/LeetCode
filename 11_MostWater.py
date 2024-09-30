# 2 Pointer approach

class Solution:
    def maxArea(self, height: list[int]) -> int:
        self.height = height
        l = 0
        r = len(self.height) - 1
        max_area = 0
        while l < r:
            w = r - l 
            area = min(self.height[l],self.height[r]) * w
            max_area = max(max_area, area)
            
            if self.height[l] < self.height[r]:
                l+=1
            else:
                r-=1
        return max_area
    
    
# User input for testing
height = list(map(int, input().split()))
result = Solution().maxArea(height)
print(result)
    

        