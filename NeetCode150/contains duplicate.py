#Brute force approach TC O(n2) SC O(1)

class Solution(object):
    def containsDuplicate(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(0,len(nums)):

            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        else:
            return False
        
#slightly better approach TC O(nlogn) SC O(1)
        
class Solution(object):
    def containsDuplicate(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        nsort = sorted(nums)
        for i in range(0,len(nums)-1):
                if nsort[i]==nsort[i+1]:
                    return True
        else:
            return False
        
#better approach TC O(n) SC O(n)
        
class Solution(object):
    def containsDuplicate(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        nset = set()

        for n in nums:
            if n in nset:
                return True
            nset.add(n)
        else:
            return False


        
