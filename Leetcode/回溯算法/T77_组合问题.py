"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""
class Solution:
    def combine(self, n, k):
        #返回值
        result = []
        self.backtracing(n, k ,1, [], result) #初始参数
        return result
    
    def backtracing(self, n, k, startindex, path, result):
        #终止条件
        if len(path) == k:
            result.append(path[:])
            return
        #单层循环，外层遍历宽度
        for i in range(startindex, n+1):
            #将当前选择加入路径
            path.append(i)
            #递归进入下一层决策树
            self.backtracing(n, k, i+1, path, result)
            path.pop() #回溯，撤销最后1个节点
