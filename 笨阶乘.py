import math
class Solution:
    def clumsy(self, N: int) -> int:
        nums = []
        opera = ['*','/','+','-']
        results = []
        res = 0
        pos = 0
        flag = 0
        for i in range(1,N+1):
            nums.append(i)
        while len(nums)!= 1:
            if pos == 0:
                a = nums.pop()
                b = nums.pop()
                nums.append(a*b)
                pos = pos + 1
            elif pos == 1:
                a = nums.pop()
                b = nums.pop()
                nums.append(math.floor(a/b))
                pos = pos + 1
            elif pos == 2:
                if flag == 0:
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(a+b)
                    pos = pos + 1
                else:
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(a-b)
                    pos = pos + 1
            elif pos == 3:
                k = nums.pop()
                results.append(k)
                flag = 1
                pos = 0
        if N <= 4:
            return nums[0]
        else:
            res = results[0]
            for i in range(1,len(results)):
                res = res - results[i]
            if nums[0]:
                res = res - nums[0]
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(5))