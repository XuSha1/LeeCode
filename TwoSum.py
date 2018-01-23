# coding=utf-8
class Solution:
    def twoSum1(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ###O(n^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
    def twoSum(self,nums,target):###O(n)
        dict={}
        for i,num in enumerate(nums):
            if num in dict:
                return [dict[num],i]
            else:
                dict[target-num]=i
                print(dict)
if __name__=='__main__':
    a=Solution()
    nums=[1,2,3,5,6]
    target=6
    print(a.twoSum(nums,target))
