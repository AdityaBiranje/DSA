class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Make min_idx the smaller index
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Option 1: remove both from left
        remove_left = right + 1

        # Option 2: remove both from right
        remove_right = n - left

        # Option 3: remove left element from left
        # and right element from right
        remove_both = (left + 1) + (n - right)

        return min(remove_left, remove_right, remove_both)