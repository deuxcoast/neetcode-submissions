from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for str in strs:
            sorted_str = sorted(str)
            signature = "".join(sorted_str)
            anagrams[signature].append(str)

        return list(anagrams.values())