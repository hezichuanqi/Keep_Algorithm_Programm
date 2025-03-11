"""
704原题
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

"""

def search_1(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

#search2:有序数组中寻找第一个target的位置
def search_2(nums, target):
    left = 0
    right = len(nums)-1
    result = -1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:#并不一定是第一个，需要寻找其左边是不是还有
            right = mid-1
            result = mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return result

#无序数组中寻找第一个target的位置
def search_3(nums, target):
    for i, num in enumerate(nums):
        if num==target:
            return i

