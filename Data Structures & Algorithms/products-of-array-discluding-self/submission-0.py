class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftArr = [1]
        curL = 1
        for i in range(1, len(nums)):
            leftArr.append(curL * nums[i-1])
            curL *= nums[i-1]

        rightArr = [0 for _ in range(len(nums))]
        rightArr[-1] = 1
        curR = 1
        for i in range(len(nums)-2, -1, -1):
            rightArr[i] = curR * nums[i+1]
            curR *= nums[i+1]

        res = []
        for i in range(len(nums)):
            res.append(leftArr[i] * rightArr[i])
        
        return res
