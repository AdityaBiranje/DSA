class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        has_nonzero = False

        for num in nums:
            xor ^= num
            if num != 0:
                has_nonzero = True

        if xor != 0:
            return n

        if not has_nonzero:
            return 0

        return n - 1