class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        group = [-1] * (m*n)
        ans = []
        count = 0
        xDirect = [1,-1,0,0]
        yDirect = [0,0,1,-1]
        for positioin in positions:
            currIndex = (positioin[0] * n) + positioin[1]
            if(group[currIndex] != -1):
                ans.append(count)
                continue
            group[currIndex] = currIndex
            count += 1
            for d in range(4):
                x = positioin[0] + xDirect[d]
                y = positioin[1] + yDirect[d]
                if x < 0 or y < 0 or x > m-1 or y > n-1:
                    continue
                destIndex = (x * n) + y

                if self.union(currIndex, destIndex,group):
                    count -= 1
        
            ans.append(count)
        return ans


    def union(self, currIndex: int, destIndex: int, group: List[int]) -> bool:
        if group[destIndex] == -1:
            return False
        currRoot = self.find(currIndex,group)
        destRoot = self.find(destIndex,group)
        if(currRoot != destRoot):
            group[currRoot] = destRoot
            return True
        return False

    def find(self, index: int,group: List[int]):
        if group[index] == index:
            return index
        return self.find(group[index],group)
        




    

            


        