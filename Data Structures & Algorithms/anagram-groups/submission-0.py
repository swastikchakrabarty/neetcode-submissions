from collections import defaultdict as dd

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dd(list)
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord('a')] += 1
            signature = tuple(count)
            groups[signature].append(s)
        return list(groups.values())