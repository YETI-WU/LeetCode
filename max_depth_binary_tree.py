# 104. Maximum Depth of Binary Tree
"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


def maxDepth(self, root):
    if not root: return 0
    return 1 + max(self.maxDepth(root.left), self.max(self.maxDepth(root.right))
    
    
# One-Line coding
def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

    
    
    
    
