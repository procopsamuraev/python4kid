class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(s)
        list_t = sorted(t)
        return list_s == list_t

#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        list_t = list(t)
#        for char in s:
#            try:
#                list_t.remove(char)
#            except:
#                return False
#        if len(list_t) != 0:
#            return False
#        else:
#            return True