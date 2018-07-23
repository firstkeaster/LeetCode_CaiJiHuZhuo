class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        A BFS Solution
        True_visited: to record if this point could be reached from all buildings, True means blocked
        visited: to record if this point is visited in curren iteration
        
        '''
        if grid == [[]]:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        True_visited = [[False] * cols for i in range(rows)]
        houses = []
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    #print(i,j)
                    True_visited[i][j] = True
                    #print(True_visited)
                    if grid[i][j] == 1:
                        houses.append((i,j,0))
                    
        
        for (i,j,_) in houses:
            visited = [x[:] for x in True_visited]
            #print('visited:',visited)
            queue = [(i,j,0)]
            #tp_counter = 0
            while queue:
                (k,l,tp_counter) = queue.pop(0)
                if visited[k][l] == False or tp_counter == 0:
                    visited[k][l] = True
                    
                    grid[k][l] -= tp_counter
                    if k-1 >= 0 and visited[k-1][l] == False:
                        queue.append((k-1,l,tp_counter+1))
                    if k+1 < rows and visited[k+1][l] == False:
                        queue.append((k+1,l,tp_counter+1))
                    if l-1 >= 0 and visited[k][l-1] == False:
                        queue.append((k,l-1,tp_counter+1))
                    if l+1 < cols and visited[k][l+1] == False:
                        queue.append((k,l+1,tp_counter+1))
            
            
            for k in range(rows):
                for l in range(cols):
                    if visited[k][l] == False:
                        True_visited[k][l] = True
                    else:
                        continue
            # print(visited)
            # print(True_visited)
            # print(grid)
            # print(True_visited)
        min_dis = -float('inf')             
        for i in range(rows):
            for j in range(cols):
                if True_visited[i][j] == False and grid[i][j] > min_dis:
                    min_dis = grid[i][j]
        if min_dis == -float('inf'):
            return(-1)
        
        return(-min_dis)
                
