class Solution(object):
    def maximalRectangle(self, matrix):
        ## DP统计每个位置上方或右边连续1数量
        ## 之后就是stack, 只有比cur低才保留
        if not matrix or not matrix[0]:
            return(0)
        m, n = len(matrix), len(matrix[0])
        res = 0
        upperOnes = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n)[::-1]:
                if i == 0:
                    upperOnes[i][j] = int(matrix[i][j] == '1')
                else:
                    upperOnes[i][j] = [0, upperOnes[i-1][j]+1][int(matrix[i][j] == '1')]
            heightsIndStack = []
            for j in range(n+1):
                if j < n:
                    curH = upperOnes[i][j]
                else:
                    curH = 0
                while heightsIndStack and \
                curH <= upperOnes[i][heightsIndStack[-1]]:
                    h = upperOnes[i][heightsIndStack.pop()]
                    formerInd = -1 if not heightsIndStack else heightsIndStack[-1]
                    res = max(res, h * (j-1-formerInd))
                heightsIndStack.append(j)
        return(res)
