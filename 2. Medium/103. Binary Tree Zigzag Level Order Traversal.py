from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])

        while q:
            length = len(q)
            level = []
            for i in range(length):
                front = q.popleft()
                level.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

            if len(level) > 0:
                if len(ans) % 2 != 0:
                    level.reverse()
                ans.append(level)
        return ans
