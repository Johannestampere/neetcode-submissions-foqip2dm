from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_counts_rn = defaultdict(int)
        letter_counts_mg = defaultdict(int)

        for c in ransomNote:
            letter_counts_rn[c] += 1

        for c in magazine:
            letter_counts_mg[c] += 1
        
        for letter in letter_counts_rn:
            if letter not in letter_counts_mg:
                return False
            
            if letter_counts_mg[letter] < letter_counts_rn[letter]:
                return False
        
        return True
