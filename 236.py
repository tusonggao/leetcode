# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isInTree(self, root, node):
        if root==None and node!=None:
            return False
        
        if not hasattr(self, 'store_isINTree'):
            self.store_isINTree = {}
        
        if (root.val, node.val) in self.store_isINTree:
            return self.store_isINTree[(root.val, node.val)]
            
        if root.val==node.val:
            self.store_isINTree[(root.val, node.val)] = True
            return True        
        
        outcome = self.isInTree(root.left, node) or self.isInTree(root.right, node)
        self.store_isINTree[(root.val, node.val)] = outcome
        return outcome
            
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val==p.val or root.val==q.val:
            return root
        
        if self.isInTree(root.left, p):
            if self.isInTree(root.right, q):
                return root
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            if self.isInTree(root.left, q):
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        
        
        
        