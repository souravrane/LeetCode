class NumMatrix {
    
    int[][] prefixMatrix;
    
    public NumMatrix(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        
        // prefix sum along rows
        for(int i = 0; i < rows; i++){
            for(int j = 1; j < columns; j++){
                matrix[i][j] += matrix[i][j-1];
            }
        }
        
        // prefix sum along columns
        for(int i = 0; i < columns; i++){
            for(int j = 1; j < rows; j++){
                matrix[j][i] += matrix[j-1][i];
            }
        }
        
        prefixMatrix = matrix;
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int ans = 0;
        
        ans +=prefixMatrix[row2][col2];
        
        if(col1 > 0){
            ans -= prefixMatrix[row2][col1-1];
        }
        
        if(row1 > 0){
            ans -= prefixMatrix[row1-1][col2];
        }
        
        if(row1 > 0 && col1 > 0){
            ans += prefixMatrix[row1-1][col1-1];
        }
        
        return ans;
    }
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */