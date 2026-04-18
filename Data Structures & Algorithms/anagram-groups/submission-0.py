from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for s in strs:
            s_sorted = " ".join(sorted(s))
            h[s_sorted].append(s)

        return list(h.values())