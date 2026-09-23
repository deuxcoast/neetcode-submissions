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
        print("encoded: ", encoded_string)
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        while idx < len(s):
            substr_length_list = []
            # read length of substring. stop at delim
            while s[idx] != self.delim:
                substr_length_list.append(s[idx])
                idx += 1

            substr_length = int("".join(substr_length_list))
            
            substr_start = idx + 1
            substr_end = substr_start + substr_length

            word = []

            for char in range(substr_start, substr_end):
                word.append(s[char])
            strs.append("".join(word))
            idx = substr_end

        return strs