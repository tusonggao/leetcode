# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#前序遍历二叉树

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            return_list = [root.val]
            return_list += self.preorderTraversal(root.left)
            return_list += self.preorderTraversal(root.right)
            return return_list
		
#中序遍历二叉树

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		if root is None:
            return []
        else:
		    return_list = self.inorderTraversal(root.left)
            return_list += [root.val]
            return_list += self.inorderTraversal(root.right)
            return return_list

#后序遍历二叉树

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		if root is None:
            return []
        else:
		    return_list = self.postorderTraversal(root.left)
			return_list += self.postorderTraversal(root.right)
            return_list += [root.val]            
            return return_list
			
#层序遍历二叉树

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        
        nodes_queue = deque()
        outcome = []
        if root:
            nodes_queue.append((root.val, 0))
        while len(nodes_queque)>0:
            val, level_num = nodes_que.popleft()
            if len(outcome)<=level_num:
                outcome.append([])
            outcome[level_num].append(val)
            if root.left:
                nodes_queue.append((root.left, level_num+1))
            if root.right:
                nodes_queue.append((root.right, level_num+1))     
        return outcome
            
            
        