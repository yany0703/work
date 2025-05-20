class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        if not root:
            return

        if root.val == p or root.val == q:
            return root.val

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        print(root.val, left, right)

        if left != None and right != None:  # 小坑! 不能用not left and not right
            return root.val
        if not right:
            return left
        if not left:
            return right



if __name__ == "__main__":
    s = Solution
    s.lowestCommonAncestor(root={7,1,12,0,4,11,14,"#","#",3,5},p=1,q=12))





    # def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
    #     def tree(self,node:TreeNode,n,m):
    #         if not node:
    #             return
    #         if node.val == n or node.val == m:
    #             return node
    #
    #         left = self.tree(node.left,n,m)
    #         right = self.tree(node.right,n,m)
    #         if not left:
    #             return right
    #         if not right:
    #             return left
    #         return node
    #     return self.tree(root,o1,o2).val
    # lowestCommonAncestor({3,5,1,6,2,0,8,"#","#",7,4},5,1)







