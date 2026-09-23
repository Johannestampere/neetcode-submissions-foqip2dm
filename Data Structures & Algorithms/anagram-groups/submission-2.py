from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for unsorted in strs:
            d["".join(sorted(unsorted))].append(unsorted)
        
        res = []
        for sorted_string in d.values():
            res.append(sorted_string)
        
        return res