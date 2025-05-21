#未剪枝版本：运行时间大概4ms
class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n,k,0,[],1,result)
        return result
    #主要在于这里的参数要想的周到
    def backtracking(self, targetsum,k,current_sum,path,startindex,result):
        #终止条件
        if len(path)==k:
            if current_sum==targetsum:
                result.append(path[:])#要特别注意这里不能直接append(path)，因为path是一个列表，是可变对象，会随着path的变化而变化
            return
        
        for i in range(startindex, 10):
            #print(current_sum)
            current_sum += i
            path.append(i)
            #print(path)
            self.backtracking(targetsum,k,current_sum,path,i+1,result)
            current_sum -= i
            path.pop()

#剪枝版本：运行时间大概0ms，速度确实变快了
class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n,k,0,[],1,result)
        return result
    #主要在于这里的参数要想的周到
    def backtracking(self, targetsum,k,current_sum,path,startindex,result):
        #终止条件
        if len(path)==k:
            if current_sum==targetsum:
                result.append(path[:])
            return
        
        for i in range(startindex, 10):
            #print(current_sum)
            current_sum += i
            path.append(i)
            if current_sum>targetsum:#剪枝
                current_sum-=i #记得要回溯回去
                path.pop()
                return
            #print(path)
            self.backtracking(targetsum,k,current_sum,path,i+1,result)
            current_sum -= i
            path.pop()