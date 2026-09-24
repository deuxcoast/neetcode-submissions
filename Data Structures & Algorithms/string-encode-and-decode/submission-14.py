class Solution:
    # use length-prefix header
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        
        #
        while i < len(s):
            j = s.index("#", i) # points to delimiter, exclusive
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            output.append(word)
            i = j + 1 + length
        
        return output

