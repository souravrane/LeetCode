class Solution:
    def isValid(self,i,j,image):
        r = len(image)
        c = len(image[0])
        return (i >= 0 and j >= 0) and (i < r and j < c)
    
    def helper(self, image, srcValue, i, j, color):
        if self.isValid(i,j,image):
            if image[i][j] != srcValue or image[i][j] == color:
                return 
            
            image[i][j] = color
            self.helper(image, srcValue, i + 1, j, color)
            self.helper(image, srcValue, i, j+1, color)
            self.helper(image, srcValue, i-1, j, color)
            self.helper(image, srcValue, i, j-1, color)

            
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.helper(image, image[sr][sc], sr, sc, color)
        return image