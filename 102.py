# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        
        nodes_que = deque()
        outcome = []
        if root:
            nodes_que.append((root, 0))
        while len(nodes_que)>0:
            node, level_num = nodes_que.popleft()
            if len(outcome)<=level_num:
                outcome.append([])
            outcome[level_num].append(node.val)
            if node.left:
                nodes_que.append((node.left, level_num+1))
            if node.right:
                nodes_que.append((node.right, level_num+1))
        return outcome