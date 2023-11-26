def inorderTraversal(root):
    if root is None:
        return []
    else:
        return inorderTraversal(root.left) + [root.val]\
            + inorderTraversal(root.right)
