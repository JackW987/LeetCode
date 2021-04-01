import math
class Solution:
    def clumsy(self,N:int) -> int:
        res = []
        res.append(N)
        N = N - 1
        index = 0
        mid = 0
        while(N > 0):
            if index % 4 == 0:
               mid = N * res.pop()
               res.append(mid)
            elif index % 4 == 1:
                if (res[-1] / N) > 0: 
                    mid = math.floor(res.pop() / N)
                else:
                    mid = math.ceil(res.pop() / N)
                res.append(mid) 
            elif index % 4 == 2:
                res.append(N)
            else:
                res.append(-N)
            N = N - 1
            index = index + 1 
        mid = 0
        for i in range(len(res)):
            mid = mid + res[i]
        return mid
if __name__=='__main__':
    s = Solution()
    print(s.clumsy(10))