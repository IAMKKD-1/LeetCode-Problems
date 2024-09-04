class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def reverse(arr):
            i=0
            j=len(arr)-1
            while i<=j:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j-=1
            return arr
        
        for i in range(len(image)):
            image[i] = reverse(image[i])
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image