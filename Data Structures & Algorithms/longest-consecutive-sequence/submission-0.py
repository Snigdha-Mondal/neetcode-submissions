class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        max_length=0
        for i in nums:
            if i-1 not in nums:
                start=i
                a=1
                subsequence_length=1
                while start+a in nums:
                    subsequence_length+=1 
                    a+=1
                if subsequence_length>max_length:
                    max_length=subsequence_length
                
        return max_length
              
        
