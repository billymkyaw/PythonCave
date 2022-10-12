#Two Sums Solution
 #Using Brute Force
 #Time Complexity: O(n^2)

 class Solution:

     def twoSum(self, nums:List[int], target: int) -> List[int]:

        for i in range (len(nums)):
         for j in range (i+1, len(nums)):
             if nums[i] + nums[j] == target:
                 return [i,j];

 #Using Hashmap
 #Time Complexity: O(n)

 class Solution:

     def twoSum(self, nums:List[int], target: int) -> List[int]:

       hashmap = {}
       for index, value in enumerate(nums):
             if value in hashmap:
                 return [hashmap[value], index]

             hashmap[target - value] = index;     #List = [2, 7, 11, 15], Target = 9
                                                  #First value = 2 => 9 - 2 = 7
                                                  # index = value
                                                  # 0 : 2
                                                  # 1 : 7
                                                  # 2 : 11
                                                  # 3 : 15
