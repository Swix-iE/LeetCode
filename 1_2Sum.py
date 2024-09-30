class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    h = {}  #initializing a hashmap

    for i, num in enumerate(nums):
      if target - num in h:
        return h[target - num], i
      h[num] = i
      
      
      
#User input test cases
nums = list(map(int, input().split()))
target = int(input())
result = list(map(int, Solution().twoSum(nums, target)))
print(result)

