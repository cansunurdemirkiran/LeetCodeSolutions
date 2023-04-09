# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def checkTree(self, root):
        sum_of_roots = root.left.val + root.right.val 

        if root.val == sum_of_roots:
            return True

        else:
            return False
