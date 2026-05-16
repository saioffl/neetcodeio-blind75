class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq = {}
        for x in t :
            freq[x] = freq.get(x,0)+1

        for x in s :
            if x in freq and freq[x] > 0 :
                freq[x] -= 1 
            else :
                return False
        
        return True
        
