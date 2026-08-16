# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float("-inf")
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            left=max(left,0)
            right=max(right,0)

            temp=max(left+node.val,right+node.val,node.val)

            self.ans=max(self.ans,temp,left+right+node.val)

            return temp

        dfs(root)
        return self.ans