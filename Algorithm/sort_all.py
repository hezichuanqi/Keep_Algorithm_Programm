#排序算法汇总
class sort_algorithm:
    def __init__(self, data):
        self.data = data
        self.len = len(data)
    
    def bubble_sort(self):
        """
        冒泡排序
        时间复杂度：最好的情况是O(n)，最坏的情况是O(n^2)
        空间复杂度：O(1)
        """
        for i in range(self.len):
            for j in range(0, self.len-i-1):
                if self.data[j]>self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def selection_sort(self):
        """
        选择排序
        时间复杂度：最好的情况是O(n^2)，最坏的情况是O(n^2)"
        """
        pass
    
    def tim_sort(self):
        """
        时间复杂度：最好的情况是O(n)，最坏的情况是O(nlogn)"
        """
        pass