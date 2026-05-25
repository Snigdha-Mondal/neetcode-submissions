class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        left_max=[0]*l
        right_max=[0]*l

        left_max[0]=height[0]
        for i in range(1,l):
            left_max[i]=max(height[i],left_max[i-1])

        right_max[l-1]=height[l-1]
        for i in range(l-2,-1,-1):
            right_max[i]=max(height[i],right_max[i+1])

        total=0
        for i in range(l):
            total+=max(0,min(left_max[i],right_max[i])-height[i])

        return total
        