class Solution:
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1.sort() #timsort
    
    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        cur = m+n-1
        #移动nums2中的元素，所以条件就是j=0
        while j>=0:
            if(i>=0 and nums1[i]>nums2[j]):
                nums1[cur] = nums1[i] #nums1大，则用nums1赋值
                cur -= 1
                i-=1
            else:
                nums1[cur]=nums2[j]
                cur -= 1
                j-=1

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge_2(nums1,3,nums2,3)