class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matches = 0
        window_count = [0] * 26
        target_count = [0] * 26
        n = len(s2); length = len(s1); match_length = len(window_count);

        if length > n:
            return False

        # target_count 초기화
        for c in s1:
            target_count[ord(c) - ord('a')] += 1
        # window_count 초기화
        for i in range(0, length):
            window_count[ord(s2[i]) - ord('a')] += 1

        # matches 초기화
        for i in range (0, match_length):
            if target_count[i] == window_count[i]:
                matches += 1


        for i in range(0, n - length + 1):
            if matches == match_length:
                return True
            
            else:
                # 빠져 나가는 문자 out_going
                out_going = ord(s2[i]) - ord('a')
                window_count[out_going] -= 1
                # 빠져 나가서 딱 맞는 경우
                if window_count[out_going] == target_count[out_going]:
                    matches += 1
                # 빠져 나갔는데, 더 적어진 경우
                elif window_count[out_going] == target_count[out_going] - 1: 
                    matches -= 1
                # 빠져 나갔는데, 과도하게 많았어서 여전히 틀린 경우는 넘어감

                # 들어오는 문자 in_coming에 대해
                if i < n - length:
                    in_coming = ord(s2[i + length]) - ord('a')
                    window_count[in_coming] += 1
                    # 들어와서 딱 맞는 경우
                    if target_count[in_coming] == window_count[in_coming]:
                        matches += 1
                    # 들어왔는데, 과해진 경우
                    elif window_count[in_coming] == target_count[in_coming] + 1:
                        matches -= 1
                    # 들어왔는데, 여전히 부족하면 넘어감

        return matches == match_length
