class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        required_map = defaultdict(int) # required char -> count
        for c in t:
            required_map[c] += 1
        
        have_map = defaultdict(int) # current window char counts

        best = float('inf')
        required = len(required_map)
        have = 0

        L_best = -1
        R_best = -1

        L = 0

        for R in range(len(s)):

            if s[R] in required_map:
                have_map[s[R]] += 1

                if required_map[s[R]] == have_map[s[R]]:
                    have += 1
                
                while have == required:

                    if R - L + 1 < best:
                        best = R - L + 1
                        L_best = L
                        R_best = R

                    if s[L] in required_map:
                        have_map[s[L]] -= 1

                        if have_map[s[L]] < required_map[s[L]]:
                            have -= 1

                    L += 1
                
        return "" if best == float('inf') else s[L_best:R_best + 1]


    

        


    

