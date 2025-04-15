def removeElement(self, nums: List[int], val: int) -> int:
        #用快慢指针解决两层for循环
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow