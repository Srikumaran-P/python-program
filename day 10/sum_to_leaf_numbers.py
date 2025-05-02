# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, path):
            if not root:
                return path
            
            ans = []
            st = [(root, path)]

            while st:
                curr, curr_path = st.pop(-1)
                # print(curr_path)
                
                if curr.left:
                    st.append((curr.left, curr_path + [curr.left.val]))

                if curr.right:
                    st.append((curr.right, curr_path + [curr.right.val]))

                if not curr.left and not curr.right:
                    ans.append(curr_path)
                    
            
            return ans

        ans = dfs(root, [root.val])

        final_ans = 0
        for path in ans:
            num = 0
            for elem in path:
                num = 10*num+ elem

            final_ans += num

        return final_ans
            
