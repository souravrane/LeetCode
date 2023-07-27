class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        for(int row = 0; row < grid.length; row++) {
            for(int col = 0; col < grid[row].length; col++) {
                if(grid[row][col] == '1') {
                    count++;
                    traverseBFS(grid, row, col);
                }
            }
        }

        return count;
    }

    private void traverseBFS(char[][] grid, int row, int col) {
        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(row);
        queue.add(col);

        while(!queue.isEmpty()) {
            row = queue.removeFirst();
            col = queue.removeFirst();
            grid[row][col] = '0';

            for(int i = 0; i < directions.length; i++) {
                int newRow = row + directions[i][0];
                int newCol = col + directions[i][1];

                if(newRow < 0 || newRow >= grid.length || newCol < 0 || newCol >= grid[0].length) {
                    continue;
                }

                if(grid[newRow][newCol] != '0') {
                    queue.add(newRow);
                    queue.add(newCol);
                    grid[newRow][newCol] = '0';
                }
            }
        }
    }
}