class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = [0] * 26; window_count = [0] * 26
        n = len(s2); length = len(s1)

        if length > n:
            return False

        for c in s1:
            target_count[ord(c) - ord('a')] += 1

        for i in range(0, len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1

        for i in range(0, n - length + 1):
            if target_count == window_count:
                return True
            else:
                window_count[ord(s2[i]) - ord('a')] -= 1

                if i + length < n: 
                    window_count[ord(s2[i+length]) - ord('a')] += 1

        return False


        

            

# Lowercase letters 만 들어오니까, counter 쓰기 좋네.
# 아, 이건 고정된 크기의 sliding window로 풀기 좋은데?
# 한 칸 씩 밀면서, s1이 있나 확인하는거지.
# sliding window의 특징은, 기존의 window의 정보를 재활용 한다니까...
