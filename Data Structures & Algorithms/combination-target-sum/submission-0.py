class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])

                # i, not i + 1, because nums[i] can be reused
                backtrack(i, remaining - nums[i], path)

                path.pop()

        backtrack(0, target, [])
        return res