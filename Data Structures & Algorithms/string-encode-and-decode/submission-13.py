class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        while idx < len(s):
            j = s.index('#', idx) # end of the length header
            length = int(s[idx:j])
            strs.append(s[j + 1 : j + 1 + length])
            idx = j + 1 + length # start of next header
        return strs