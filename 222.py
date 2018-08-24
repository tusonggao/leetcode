# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.last_but_one_level_nodes = []
        self.LAST_NODE_FOUND = False
    
    #得到height层所有的node，按照从左到右的顺序，
    #按照完全二叉树定义，如果碰到一个节点的子节点为空，便可以停止搜索了
    def get_childs_by_level(self, root, height, current_height):
        if self.LAST_NODE_FOUND:
            return
        if root is None:
            return
        
        if current_height==height:
            self.last_but_one_level_nodes.append(root)
            if root.left is None or root.right is None:
                self.LAST_NODE_FOUND = True
        elif current_height<height:
            self.get_childs_by_level(root.left, height, current_height+1)
            self.get_childs_by_level(root.right, height, current_height+1)
    
    #计算二叉树高度，根据完全二叉树定义，只需要搜索左子节点即可
    def countTreeHeight(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.countTreeHeight(root.left)
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        tree_height = self.countTreeHeight(root)
        if tree_height==0:
            return 0
        elif tree_height==1:
            return 1
        
        #收集得到所有倒数第二层的node,按照从左到右的顺序
        self.get_childs_by_level(root, tree_height-1, 1)
        
        nodes_num = 2**(tree_height-1) - 1 + len(self.last_but_one_level_nodes)*2
        if self.last_but_one_level_nodes[-1].left==None:
            nodes_num -= 2
        elif self.last_but_one_level_nodes[-1].right==None:
            nodes_num -= 1
            
        return nodes_num
        