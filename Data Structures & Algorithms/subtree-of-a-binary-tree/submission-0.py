# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def recursion(root1, subRoot1):

            if root1 is None and subRoot1 is None:
                return True

            if root1 is None or subRoot1 is None:
                return False

            if root1.val != subRoot1.val:
                return False
            
            return (recursion(root1.left, subRoot1.left) and recursion(root1.right, subRoot1.right))
        
        if subRoot is None:
            return True

        if root is None:
            return False

        if recursion(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )