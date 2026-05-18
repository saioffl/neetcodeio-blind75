from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # {1:1 , 2:2 , 3:3}
        
        mostFreq = counter.most_common(k)
        result = []
        for value,freq in mostFreq :
            result.append(value)
        
        return result
        



            
        