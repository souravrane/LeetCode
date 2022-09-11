class Solution:
    def helper(self, image, i, j, src, color):
        if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == src and image[i][j] != color:
            image[i][j] = color
            dx= [-1,1,0,0]
            dy = [0,0,-1,1]
            for k in range(4):
                self.helper(image, i + dx[k], j + dy[k], src, color)
            
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.helper(image, sr, sc, image[sr][sc], color)
        return image