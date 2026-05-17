from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)

        for x in strs :
            sortedList = "".join(sorted(x))

            lists[sortedList].append(x)
        return list(lists.values())
        