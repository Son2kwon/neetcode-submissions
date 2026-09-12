class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0; high = 0
        
        for i, c in enumerate(s):
            if c == "*":
                low = max(low - 1, 0); high += 1

            elif c == "(":
                low += 1; high += 1

            elif c == ")":
                low = max(low - 1, 0); high -= 1

                if high < 0: return False

        return low == 0


# *을 어떻게 해석할 것인가에 따라 달라지겠네. 근데 이거 저번에 푼 정규식 문제랑 비슷하지 않나? 물론 DP긴 했지만
# 그리고 괄호 숫자 맞추는 건 stack으로 하면 편한데

# 그러면 stack으로 push, pop을 해버릴까?
# *을 만나면 그냥 (로도 한번 넘겨보고, )로도 한 번 넘겨보고, 빈 문자로도 넘겨보고

# 힌트1: *를 만났을 때 brute force로 풀면 exponential. parenthesis problems에서 자주 쓰이는 자료구조가 도움이 될 듯?
# 그게 stack이잖아

# 힌트2: stack-based approach로 풀 수 있다: 하나는 parentheses, 하나는 *
# 아, *을 저장하는 stack을 하나 써서, 필요할 때 꺼내쓴다 이런 건가?

# 근데 단순하게 숫자만 세기에는 순서를 무시하는 것이라... 순서까지 신경 쓰면서 하려면 어떻게 해야할까?
# stack이랑 star에 [(, idx], [*, idx]를 넣는 방법이 있긴 하겠네. 그리고 stack의 idx 보다 *의 idx가 클 때만 빼는거지.

# Time Complexity: O(n)
# Space Complexity: O(n)