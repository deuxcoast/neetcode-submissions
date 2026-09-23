class Solution:
    delim = "#"
    def encode(self, strs: List[str]) -> str:
        word_list = []
        for word in strs:
            length = len(word)
            char_list = [str(length), self.delim]
            for char in word:
                char_list.append(char)
            encoded_word = "".join(char_list)
            word_list.append(encoded_word)
        
        encoded_string = "".join(word_list)
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        while idx < len(s):
            j = s.index('#', idx) # end of the length header
            length = int(s[idx:j])
            strs.append(s[j + 1 : j + 1 + length])
            idx = j + 1 + length # start of next header
        return strs