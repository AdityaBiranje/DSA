class Solution:
    def sumAndMultiply(self, n: int) -> int:
        concat = 0
        total = 0
        place = 1

        while n > 0:
            digit = n % 10

            if digit != 0:
                concat += digit * place
                total += digit
                place *= 10

            n //= 10

        return concat * total