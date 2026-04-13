class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left = 0
        n = len(s)
        ret = 0

        def is_valid(length):
            nonlocal counter, k
            return (length-max(counter.values()))<=k

        for right in range(n):
            counter[s[right]] += 1
            while not is_valid(right-left+1):
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            ret = max(ret, right-left+1)
        return ret
