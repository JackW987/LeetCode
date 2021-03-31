class Solution:
    def generateMatrix(self, n):
        sum = n**2
        list_n = [[0 for i in range(n)] for j in range(n)]
        row = 0
        val = 1
        pos = n-1
        ran = n-1
        if n%2 == 0:
            total = int(n/2)
        else:
            total = int(n/2)+1
            list_n[int(n/2)][int(n/2)] = sum
        for i in range(total):
            print(pos)
            for j in range(4):
                for k in range(ran):
                    if j == 0:
                        list_n[row][row+k] = val
                        val = val + 1
                        print('k:',k,'pos',pos,'list_n:',list_n[row][row+k])
                    if j == 1:
                        list_n[row+k][pos] = val
                        val = val + 1
                        print('k:',k,'pos',pos,'list_n:',list_n[k][pos])
                    if j == 2:
                        list_n[pos][pos-k] = val
                        val = val + 1
                        print('k:',k,'pos',pos,'list_n:',list_n[pos][pos-k])
                    if j == 3:
                        list_n[pos-k][row] = val
                        val = val + 1
                        print('row:',row,'pos-k:',pos-k,'list_n:',list_n[pos-k][row])
            row = row + 1
            pos = pos - 1
            ran = ran - 2
        return list_n
 
#优质解答
# class Solution {
#     public int[][] generateMatrix(int n) {
#         int[][] arr = new int[n][n];
#         int c = 1, j = 0;
#         while (c <= n * n) {
        
#             for (int i = j; i < n - j; i++)
#                 arr[j][i] = c++;
#             for (int i = j + 1; i < n - j; i++)
#                 arr[i][n - j - 1] = c++;
#             for (int i = n - j - 2; i >= j; i--)
#                 arr[n - j - 1][i] = c++;
#             for (int i = n -j - 2; i > j; i--)
#                 arr[i][j] = c++;

#             j++;
#         }

#         return arr;
#     }

# }