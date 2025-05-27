class Solution:
    def __init__(self):
        #构建字典的映射
        self.lettermap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.result = []
        self.s = "" #注意这里不能有空格
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return self.result
        self.backtracking(digits, 0)
        return self.result

    def backtracking(self, digits, index):
        #回溯最好是能画图去解决问题
        #终止条件
        if index==len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index]) #字符转为整数
        letters = self.lettermap[digit] #1个index会对应几个字母
        #单次遍历
        for i in range(len(letters)):
            self.s+=letters[i] #字符串不能使用append
            self.backtracking(digits, index+1) #注意index和i的关系
            self.s = self.s[:-1] #对于字符串的回溯