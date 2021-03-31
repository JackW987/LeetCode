class Solution(object):
    def recur(self,s,t,pos,now,end,count):
        w = pos        
        now = now + 1
        print('now:',now,'pos:',pos)
        print('s[now]:',s[now],'t[pos]:',t[pos])
        if pos!=(len(t)-1):    
            for j in range(now,end):
                if s[j] == t[w]:
                    now = j
                    w = w + 1 
                    self.recur(s,t,w,now,end,count)
        else:
            count = count + 1
            print('pass############')
            return count
    def numDistinct(self, s, t):
        count = 0
        pos = 0
        end = len(s)-1
        for i in range(len(s)):
            if s[i] == t[pos]:
                now = i
                c = pos + 1
                self.recur(s,t,c,now,end,count)

if __name__ == '__main__':
    k = Solution()
    k.numDistinct('rabbbit','rabbit')