class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        l=len(temperatures)
        result=[0]*l
        
        for i in range(l):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                idx=stack.pop()
                result[idx]=i-idx
            stack.append(i)

        return result
