from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sig = [0]*26
            for char in word:
                sig[ord(char) - ord('a')] += 1
            sig = tuple(sig)
            anagram_map[sig].append(word)
        
        return list(anagram_map.values())
        