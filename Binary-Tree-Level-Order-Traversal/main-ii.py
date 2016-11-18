#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        roots = [root]
        result = []
        while roots:
            next_roots = []
            values = []
            for r in roots:
                values.append(r.val)
                if r.left: next_roots.append(r.left)
                if r.right: next_roots.append(r.right)
            roots = next_roots
            result.append(values)
        return result[::-1]

    def pre_print(self, root):
        if not root: return None
        print root.val
        self.pre_print(root.left)
        self.pre_print(root.right)


import random
randint = random.randint
def gen_treenode(root, deep=5):
    deep -= 1
    if deep == 0: return root
    root.left = TreeNode(randint(1, 50))
    root.right = TreeNode(randint(1, 50))
    gen_treenode(root.left, deep)
    gen_treenode(root.right, deep)
    return root


if __name__ == '__main__':
    test_data = TreeNode(3)
    test_data.left = TreeNode(9)
    test_data.right = TreeNode(20)
    test_data.right.left = TreeNode(15)
    test_data.right.right = TreeNode(7)
    test_data = gen_treenode(TreeNode(30), deep=20)
    print Solution().levelOrderBottom(test_data)
