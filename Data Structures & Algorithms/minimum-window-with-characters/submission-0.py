class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        t_counter = collections.Counter(t)
        left = 0

        def is_valid(s_counter, t_counter):
            for k in t_counter.keys():
                if t_counter[k]>s_counter[k]:
                    return False
            return True

        ret = ''
        s_counter = collections.Counter()
        for right in range(n):
            s_counter[s[right]] += 1
            while is_valid(s_counter, t_counter):
                if not ret or (right-left+1)<len(ret):
                    ret = s[left:right+1]
                s_counter[s[left]] -= 1
                left += 1
        return ret