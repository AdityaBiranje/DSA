class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        # Count characters
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # More than one odd count -> palindrome impossible
        odd = [i for i in range(26) if freq[i] % 2]

        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else -1

        # Only half of each character is needed
        for i in range(26):
            freq[i] //= 2

        n = len(s)
        half = n // 2
        ans = [''] * n

        # Build palindrome from first half
        def make_palindrome():
            if mid != -1:
                ans[half] = chr(ord('a') + mid)

            for i in range(half):
                ans[n - 1 - i] = ans[i]

        pos = 0

        # First, try to keep the prefix equal to target
        while pos < half:
            idx = ord(target[pos]) - ord('a')

            if freq[idx] == 0:
                break

            ans[pos] = target[pos]
            freq[idx] -= 1
            pos += 1

        # Entire first half matched target
        if pos == half:
            make_palindrome()

            candidate = ''.join(ans)

            if candidate > target:
                return candidate

        # Backtrack and increase the rightmost possible position
        while True:

            # Try to make current position strictly larger
            if pos < half:
                start = ord(target[pos]) - ord('a') + 1

                for ch in range(start, 26):
                    if freq[ch] > 0:

                        ans[pos] = chr(ord('a') + ch)
                        freq[ch] -= 1

                        # Fill remaining half with smallest chars
                        idx = pos + 1

                        for c in range(26):
                            for _ in range(freq[c]):
                                ans[idx] = chr(ord('a') + c)
                                idx += 1

                        make_palindrome()

                        return ''.join(ans)

            # Can't increase here -> backtrack
            if pos == 0:
                return ""

            pos -= 1

            # Restore the character used at this position
            idx = ord(target[pos]) - ord('a')
            freq[idx] += 1