# tC O(m*n) SC (m*n)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) # mapping char count to list of anagrams
        
        for s in strs:
            count =  [0] * 26 
            for c in s:
                count[ord(c)-ord("a")] =+ 1
            res[tuple(count)].append(s) # list cannot be keys in Dictionary
        return res.values()
