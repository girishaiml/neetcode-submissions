
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack()

                # Backtrack
                path.pop()
                used[i] = False

        backtrack()
        return res