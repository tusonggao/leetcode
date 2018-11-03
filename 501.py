# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#需要使用额外空间的解法

class Solution:
    def traversal(self, root):
        if root==None:
            return
        if root.val in self.count_store:
            self.count_store[root.val] += 1
        else:
            self.count_store[root.val] = 1
        self.traversal(root.left)
        self.traversal(root.right)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        
        self.count_store = {}
        self.traversal(root)
        
        max_num = max(self.count_store.values())
        result = []
        for k in self.count_store:
            if self.count_store[k]==max_num:
                result.append(k)
        return result

#################################################################################
		
#不需要使用额外空间的解法
            
        