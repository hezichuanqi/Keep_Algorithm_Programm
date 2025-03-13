class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #记录迭代中最近一次0的位置
        lastzero = -1
        lens = 0
        for i, num in enumerate(nums):
            if num!=1: #nums==0也行
                lastzero=i
            else:
                lens = max(lens, i-lastzero)
        return lens