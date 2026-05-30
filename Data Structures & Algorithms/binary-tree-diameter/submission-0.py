# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam=0
        if root is None:
            return 0
        def depth(node):
            if node is None:
                return 0
            self.diam=max(self.diam,depth(node.left)+ depth(node.right) )
            return 1+ max(depth(node.left), depth(node.right))
        depth(root)
        return self.diam