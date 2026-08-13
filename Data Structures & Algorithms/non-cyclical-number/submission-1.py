class Solution:
    def returnSum(self, n: int) -> int:
        returnValue = 0

        while n > 0:
            returnValue += (n % 10) * (n % 10)
            n //= 10

        return returnValue

    def isHappy(self, n: int) -> bool:
        fast = self.returnSum(n)
        slow = n

        while fast != slow:
            fast = self.returnSum(self.returnSum(fast))
            slow = self.returnSum(slow)

        if fast == 1:
            return True
        else:
            return False
        

# 그냥 계속 돌려봐야하나..?

# True: 1, 10, 100, 1000, 7
# False: 2, 3, 4, 5, 6, 8, 9

# 0^2 ~ 9^2 의 합으로 표현되는 값이 중요함. 1 4 9 16 25 36 49 64 81
# 그러면, 그 합이 1, 10, 100, 1000이 되는지 확인하면 된다.
# 1이 되는 경우는 10, 100, 1000
# 10이 되는 경우는 1^2 + 3^2
# 100이 되는 경우는 
# 1000이 되는 경우는 

# 9 -> 81 -> 65 -> 41 -> 17 -> 50 -> 25 -> 29 -> 85 ->  89

# 왜 뭔가 규칙이 보이는 것 같지, 나오는 숫자들이 비슷비슷한데?

# 999 -> 243 -> 29
# 998 -> 226 -> 44 -> 32 -> 13 -> 10
# 997 -> 211 -> 6 -> 36 -> 45 -> 41

# 99 -> 162 -> 41
# 98 -> 145