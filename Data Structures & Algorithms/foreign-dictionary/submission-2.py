class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        seen = set()
        degree = [0]*26
        children = [[] for _ in range(26)]

        for i in range(0, n-1):
            for c1, c2 in zip_longest(words[i], words[i+1]):
                if c1 == c2: continue
                if c1 is None: break
                if c2 is None: return ''
                else:
                    keya = ord(c1)-ord('a')
                    keyb = ord(c2)-ord('a')
                    degree[keyb] += 1
                    children[keya].append(keyb)
                    break
        for i in range(n):
            for c in words[i]:
                key = ord(c)-ord('a')
                seen.add(key)

        q = collections.deque()
        for i in range(26):
            if i not in seen: continue
            if degree[i] != 0: continue
            q.append(i)

        ret = []
        while q:
            i = q.popleft()
            ch = chr(i+ord('a'))
            ret.append(ch)
            for j in children[i]:
                degree[j] -= 1
                if degree[j] != 0: continue
                q.append(j)
        return ''.join(ret) if len(ret) == len(seen) else ''

