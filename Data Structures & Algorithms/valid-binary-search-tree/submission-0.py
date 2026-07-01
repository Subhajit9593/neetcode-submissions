# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lb,ub):
            if node is None:
                return True
            if node.val<=lb or node.val>=ub:
                return False
        
            return dfs(node.left,lb,node.val) and dfs(node.right,node.val,ub)
            
            
        return dfs(root,float("-inf"),float("inf"))