class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        sum = 0
        k = x
        while k > 0:
            sum += k % 10
            k = k // 10

        if x % sum == 0:
            return sum
        return -1
