from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        for j in range(n):
            min_b = pow(10,11)
            max_a = pow(-10,11)
            for i in range(j):
                if nums[i]<nums[j] and nums[i]<min_b:
                    min_b = nums[i]
                    if (i+1)<j and nums[i+1] <min_b:
                        min_b = nums[i+1]
            for k in range(j+1,n):
                if nums[k]<nums[j] and nums[k]>max_a:
                    max_a = nums[k]
                    if (k+1)<(n) and nums[k+1] > max_a and nums[k+1]<nums[j]:
                        max_a = nums[k+1]
            if max_a > min_b and max_a < nums[j] and nums[j] > min_b:
                return True
        return False
if __name__ =='__main__':
    s = Solution()
    # print(s.find132pattern([])