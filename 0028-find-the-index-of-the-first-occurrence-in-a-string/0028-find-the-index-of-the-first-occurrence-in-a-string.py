class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build LPS (Longest Prefix Suffix) array
        lps = [0] * len(needle)

        length = 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1

        # KMP search
        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return i - j

            elif j:
                j = lps[j - 1]
            else:
                i += 1

        return -1
        