# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归解法

class Solution(object):
    def isSymmetricEqualTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return (self.isSymmetricEqualTree(root1.left, root2.right) and
                self.isSymmetricEqualTree(root1.right, root2.left))
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricEqualTree(root.left, root.right)

		
#################################################################################

# 迭代解法
class Solution(object):    
    def isSymmetric(self, root):
        if root is None:
            return True
        if not root.left and not root.right:
            return True
        
        left_v_list = [root.left]
        right_v_list = [root.right]
        idx = -1
        
        while True:
            if len(left_v_list)!=len(right_v_list):
                return False
            
            idx += 1
            if idx > (len(left_v_list) - 1):
                break
                
            left_v = left_v_list[idx]
            right_v = right_v_list[idx]
            
            if left_v is not None:
                left_v_list.append(left_v.left)
                left_v_list.append(left_v.right)
            
            if right_v is not None:
                right_v_list.append(right_v.right)
                right_v_list.append(right_v.left)
                    
            if type(left_v)==TreeNode and type(right_v)==TreeNode and left_v.val!=right_v.val:
                return False
            if left_v is None and right_v is not None:
                return False
            if left_v is not None and right_v is None:
                return False
            
        return True









