# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node: TreeNode) -> tuple:
            if not node:
                return None, 0

            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            if left_depth < right_depth:
                return right_node, right_depth + 1
            elif left_depth == right_depth:
                return node, left_depth + 1
            else:
                return left_node, left_depth + 1

        return dfs(root)[0]