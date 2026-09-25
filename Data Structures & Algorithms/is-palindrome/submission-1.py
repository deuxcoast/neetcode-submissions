class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1   

        while i < j:
            left, right  = s[i], s[j]
            while i < j and not left.isalnum():
                i += 1
                left = s[i]
            while i < j and not right.isalnum():
                j -= 1
                right = s[j]
            left = left.casefold()
            right = right.casefold()
            if left != right:
                return False
            i += 1
            j -= 1
            
        return True