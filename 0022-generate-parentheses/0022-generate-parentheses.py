class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, open, close):
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            # Add '('
            if open < n:
                path.append("(")
                backtrack(path, open + 1, close)
                path.pop()

            # Add ')'
            if close < open:
                path.append(")")
                backtrack(path, open, close + 1)
                path.pop()

        backtrack([], 0, 0)

        return ans