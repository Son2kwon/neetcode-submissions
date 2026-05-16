class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_pointer = 0; s_list = list(s); s_list.sort(); len_s = len(s)
        t_pointer = 0; t_list = list(t); t_list.sort(); len_t = len(t)

        while s_pointer < len_s and t_pointer < len_t:
            if s_list[s_pointer] != t_list[t_pointer]:
                return False
            s_pointer += 1
            t_pointer += 1

        return s_pointer == len_s and t_pointer == len_t