class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isSubtree(self, root: TreeNode|None, subroot: TreeNode|None) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        if self.sametree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)


    def sametree(self, p: TreeNode|None, q:TreeNode|None):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return  self.sametree(p.left, q.left) and self.sametree(p.right, q.right)
    
