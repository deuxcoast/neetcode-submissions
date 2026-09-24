from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            signature = [0] * 26
            for char in word:
                signature[ord(char) - ord('a')] += 1
            signature = tuple(signature)
            anagram_map[signature].append(word)
        
        return [x for x in anagram_map.values()]