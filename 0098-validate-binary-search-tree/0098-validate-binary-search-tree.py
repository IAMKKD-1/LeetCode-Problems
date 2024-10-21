# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxxl = maxxr = 0

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(root, min_val, max_val):
            if not root:
                return True
            
            if root.val <= min_val or root.val >= max_val:
                return False
            
            left = check(root.left, min_val, root.val)
            right = check(root.right, root.val, max_val)

            return left and right
        
        return check(root, float('-inf'), float('inf'))