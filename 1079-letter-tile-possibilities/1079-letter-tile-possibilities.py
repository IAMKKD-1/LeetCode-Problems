class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        data = set()
        visited = [False]*len(tiles)

        def search(seq, depth):
            if len(seq) != 0:
                data.add(seq)
            
            if depth == len(tiles):
                return

            for i in range(len(tiles)):
                if visited[i] == False:
                    visited[i] = True
                    search(seq+tiles[i], depth+1)
                    visited[i] = False
            
        search('', 0)
        return len(data)