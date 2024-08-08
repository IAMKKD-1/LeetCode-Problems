class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        data = set()
        for i in paths:
            data.add(i[0])
        for i in paths:
            if i[1] not in data:
                return i[1]
                