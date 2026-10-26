# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])  # initialize queue with root node

        # fmt: off
        while q:
            n = len(q) # number of nodes at current level, so we can iterate through all of them and add their children to the queue for the next level
            level = []
            for i in range(n): # runs n times, where n is the number of nodes at the current level
                front = q.popleft()
                level.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            ans.append(level)
        return ans
