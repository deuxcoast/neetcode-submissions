class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consec = 0

        for num in num_set:
            if num-1 not in num_set:
                consec = 1
                curr_num = num+1
                while curr_num in num_set:
                    consec += 1
                    curr_num += 1
                if consec > max_consec:
                    max_consec = consec
        return max_consec
                

