class Solution:
    def reverseBits(self, n: int) -> int:
        mid_val = bin(n).replace('0b','')
        list_val = list(mid_val)
        val_l = len(list_val)
        list_add = []
        for i in range(32-val_l):
            list_val.insert(0,'0')
        list_final = []
        for i in range(len(list_val)-1,-1,-1):
            list_final.append(list_val[i])
        mid_final_val = ''.join(list_final)
        final = int(mid_final_val,2)
        print(mid_val)
        print(mid_final_val)
        return final
if __name__=='__main__':
    s = Solution()
    s.reverseBits(43261596)