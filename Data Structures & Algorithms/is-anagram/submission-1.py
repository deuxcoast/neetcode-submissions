from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        if len(s_count) != len(t_count):
            return False
        for char, count in s_count.items():
            if t_count[char] != count:
                return False
        return True