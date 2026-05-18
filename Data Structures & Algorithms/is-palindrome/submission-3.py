class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbols = set()
        s = s.lower()
        s = s.replace(" ", "")

        for c in s:
            if not c.isalnum() and c not in symbols:
                symbols.add(c)

        for c in s:
            if c in symbols:
                s = s.replace(c, "")

        left = 0; right = len(s) - 1;
        print(s)
        while left < right:
            if s[left] != s[right]: return False

            left += 1; right -= 1;

        return True

# 문자열에서 Alphanumeric characters를 제외하고 나머지는 제거한 후에 two pointer로 풀기
# 특수 문자 종류가 뭐가 있는지 모르니... 한 번 순회하면서 symbols 변수에 담고 모두 제거 후 two pointers