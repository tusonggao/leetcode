# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归版本解答

class Solution:
    def greatestVal(self, root):
        if not hasattr(self, 'store_greatestVal'):
            self.store_greatestVal = {}
            
        if root in self.store_greatestVal:
            return self.store_greatestVal[root]
        
        node = root
        while node.right:
            node = node.right
        self.store_greatestVal[root] = node.val
        return node.val
    
    def smallestVal(self, root):
        if not hasattr(self, 'store_smallestVal'):
            self.store_smallestVal = {}
            
        if root in self.store_smallestVal:
            return self.store_smallestVal[root]
        
        node = root
        while node.left:
            node = node.left
        self.store_smallestVal[root] = node.val
        
        return node.val
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        
        left_BST, right_BST = False, False
        
        if root.left:
            if self.greatestVal(root.left) < root.val and self.isValidBST(root.left):
                left_BST = True
        else:
            left_BST = True
            
        if root.right:
            if self.smallestVal(root.right) > root.val and self.isValidBST(root.right):
                right_BST = True
        else:
            right_BST = True
        
        return left_BST and right_BST
                
################################################################################################

# 迭代版本解答

class Solution:        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        
        stack = [root]
        val_last = -float('inf')
        
        while len(stack)>0:
            last_ele = stack.pop()
            if type(last_ele)==TreeNode:
                if last_ele.right:
                    stack.append(last_ele.right)
                stack.append(last_ele.val)
                if last_ele.left:
                    stack.append(last_ele.left)
            else:
                if val_last >= last_ele:
                    return False
                else:
                    val_last = last_ele
        
        return True



