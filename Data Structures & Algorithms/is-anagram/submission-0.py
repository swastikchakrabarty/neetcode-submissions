from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Counter("rat") creates {'r': 1, 'a': 1, 't': 1}
        return Counter(s) == Counter(t)