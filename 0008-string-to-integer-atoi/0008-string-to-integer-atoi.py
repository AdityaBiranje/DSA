class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Handle empty string after spaces
        if i == n:
            return 0

        # Handle sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        # Read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Overflow check
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            num = num * 10 + digit
            i += 1

        return sign * num