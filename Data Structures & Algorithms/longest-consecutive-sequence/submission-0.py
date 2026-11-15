class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        streak = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            elif nums[i] == nums[i - 1] + 1:
                streak += 1  # Consecutive number

            else:
                streak = 1  # Sequence broken, start again

            res = max(res, streak)

        return res

        