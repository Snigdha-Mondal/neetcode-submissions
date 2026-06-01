class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r=0,0
        output=[]
        q=collections.deque()

        while r <len(nums):
            #pop smaller values from q
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            #remove leftmost elememt if it is out of bounds of the window
            if l>q[0]:
                q.popleft()

            if (r+1)>=k:
                
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output