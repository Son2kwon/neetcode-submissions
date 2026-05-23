class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s); len_t = len(t);
        
        # 길이가 작다면 substring 만들 수 없음
        if len_s < len_t:
            return ""

        left = 0; right = 0;

        target_count = defaultdict(int); window_count = defaultdict(int)

        for c in t:
            target_count[c] += 1

        required = len(target_count.keys()); formed = 0; ans = 1001;
        ans_left = len_s; ans_right = 0;
        
        while right < len_s:

            c_right = s[right]
            # 만약 현재 값이 target_count에 있으면
            if c_right in target_count:
                window_count[c_right] += 1
                # window_count와 target_count의 값이 같아지면 formed += 1
                if window_count[c_right] == target_count[c_right]:
                    formed += 1
            # required == formed라면, left를 계속 옮겨줌
            while required == formed:
                # ans의 현재 길이 > window 길이
                if ans > right - left + 1:
                    ans_left = left
                    ans_right = right
                    ans = ans_right - ans_left + 1

                c_left = s[left]
                if c_left in target_count:
                    window_count[c_left] -= 1

                    if window_count[c_left] < target_count[c_left]:
                        formed -= 1

                print("left: ", left, "right: ", right)
                print("ans: ", ans)
                print("ans_left: ", ans_left, "ans_right: ", ans_right)

                left += 1

            right += 1

        if ans_left > ans_right:
            return ""

        return s[ans_left: ans_right + 1]


        
# Test Case를 돌려보니까, 최소 사용 조건이 있네.
# count를 사용하는데, 중복은 어떻게 처리하지..?

# count를 다 쓸 때까지 right을 쭉 이동
# left를 count가 망가지지 않는 선까지 움직이면서 ans 업데이트

# window_count >= target_count 인 경우에 성공