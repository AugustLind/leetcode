class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.search(root, [])

    def search(self, root: TreeNode | None, result: list[int]) -> list[int]:

        if root is None:
            return result

        if root.left is not None:
            result = self.search(root.left, result)

        result.append(root.val)

        if root.right is not None:
            result = self.search(root.right, result)

        return result
