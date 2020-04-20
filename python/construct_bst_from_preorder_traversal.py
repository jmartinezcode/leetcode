# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, 
# any descendant of node.left has a value < node.val, and any descendant 
# of node.right has a value > node.val.  Also recall that a preorder traversal 
# displays the value of the node first, then traverses node.left, then traverses 
# node.right.)

 

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

 

# Note: 

# 1 <= preorder.length <= 100
# The values of preorder are distinct.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        
        root = TreeNode(preorder[0])
        
        def helper(val, root):
            
            while True:
                if root.val > val:
                    if not root.left:
                        root.left = TreeNode(val)
                        break
                    else:
                        root = root.left
                else:
                    if not root.right:
                        root.right = TreeNode(val)
                        break
                    else:
                        root = root.right
        
        top = root
        
        for i in range(1, len(preorder)):
            #reset pointer to top of tree
            top = root
            helper(preorder[i], top)
        return top