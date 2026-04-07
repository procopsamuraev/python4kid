import time

# time=time.time()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = []
        for char in s:
            if char.isalnum():
                s_new.append(char.lower())
        if not s_new: 
            return True
        for char in s_new:
            if char != s_new.pop():
                return False
        return True
start_time = time.perf_counter()

check1 = Solution().isPalindrome('aabbcc')

end_time = time.perf_counter()
time_elapsed = end_time - start_time
print(check1, time_elapsed)