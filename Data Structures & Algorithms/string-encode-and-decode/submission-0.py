class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ret = []
        for s in strs:
            ret.append('|')
            ret.append(str(len(s)))
            ret.append('|')
            ret.append(s)
        return ''.join(ret)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        n = len(s)
        i = 1
        len_str = ''
        ret = []
        print(s)
        while i<n:
            if s[i] == '|':
                len_int = int(len_str)
                len_str = ''
                ret.append(s[i+1:i+1+len_int])
                i += len_int + 1
            else:
                len_str += s[i]
            i += 1
        return ret





