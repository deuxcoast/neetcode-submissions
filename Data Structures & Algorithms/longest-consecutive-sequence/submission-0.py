class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_consec = 0
        for num in nums:
            if (num - 1) not in num_set:
                
                consec = 0
                x = num
                while x in num_set:
                    consec += 1
                    x = x + 1
            
                if consec > max_consec:
                    max_consec = consec
        return max_consec

            


          
