class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      
        mapp = {} 

        for i, n in enumerate(nums):
            diff = target - n
            
            # O(1) Lookup in Map (Slide 80)
            if diff in mapp:
                return [mapp[diff], i]
            
            # Store the current number in the Map for later
            mapp[n] = i