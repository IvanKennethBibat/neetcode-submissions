import operator

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) == len(t):

            for char in s:
                seen[char] = seen.get(char, 0) + 1
            
            for char in t:
                seen[char] = seen.get(char,0) - 1
            
            for value in seen.values():
                if value > 0:
                    return False
            return True
            
        return False
        


        