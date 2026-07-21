from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        required_counts = Counter(t)
        window_counts = defaultdict(int)

        required = len(required_counts)
        formed = 0

        left = 0
        best_length = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window_counts[char] += 1

            # This character's required frequency is now satisfied.
            if (
                char in required_counts
                and window_counts[char] == required_counts[char]
            ):
                formed += 1

            # Shrink the valid window from the left.
            while formed == required:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                left_char = s[left]
                window_counts[left_char] -= 1
                left += 1

                # Removing this character made the window invalid.
                if (
                    left_char in required_counts
                    and window_counts[left_char] < required_counts[left_char]
                ):
                    formed -= 1

        if best_length == float("inf"):
            return ""

        return s[best_start : best_start + best_length]