class Solution:
    # use length-prefix header
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        
        # i points to the very beginning of the current chunk's length prefix.
        # invariant: at the start of every iteration, i is exactly at the 
        # beginning of a new encoded chunk.
        while i < len(s):
            # j: Points directly to the '#' delimiter of the current chunk.
            j = s.index("#", i)

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            output.append(word)

            # move i to the first character of the next chunk
            i = j + 1 + length
        
        return output

