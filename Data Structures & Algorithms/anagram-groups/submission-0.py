class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        visited = dict()

        def str_to_counter_key(s):
            counter = collections.Counter(s)
            ret = ''
            for k in sorted(counter.keys()):
                ret += f"{k}{counter[k]}"
            return ret

        for s in strs:
            k = str_to_counter_key(s)
            if k in visited:
                visited[k].append(s)
            else:
                v = [s]
                visited[k] = v
                ret.append(v)
        return ret

