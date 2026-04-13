class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1: return False

        counter_s1 = collections.Counter(s1)
        counter_s2 = collections.Counter(s2[:n1])
        diff_keys = set()
        for k in counter_s1.keys():
            if counter_s1[k] == counter_s2[k]:
                continue
            diff_keys.add(k)
        if len(diff_keys) == 0: return True

        for i in range(n1, n2):
            counter_s2[s2[i]] += 1
            counter_s2[s2[i-n1]] -= 1
            if counter_s1[s2[i]] == counter_s2[s2[i]]:
                diff_keys.discard(s2[i])
            else:
                diff_keys.add(s2[i])
            if counter_s1[s2[i-n1]] == counter_s2[s2[i-n1]]:
                diff_keys.discard(s2[i-n1])
            else:
                diff_keys.add(s2[i-n1])
            if len(diff_keys) == 0: return True

        return False