class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        di = 0
        
        for i in range(len(nums)):
            if nums[di]==0:
                nums.pop(di)
                nums.insert(0,0)
                di = di+1
            elif nums[di]==2:
                nums.pop(di)
                nums.append(2)
            else:
                di = di+1
        return