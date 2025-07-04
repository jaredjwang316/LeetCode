#include <iostream>
#include <vector>

using namespace std;

/**
 * Problem Description:
    * You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 
    * 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
    * The area of an island is the number of cells with a value 1 in the island.
    * Return the maximum area of an island in grid. If there is no island, return 0.
 *
 * Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 50
    * grid[i][j] is either 0 or 1.
 */

class Solution {
public:
    int count = 0;
    int maxArea = 0;

    void dfs(vector<vector<int>>& grid, int row, int col)   {
        if (row < 0 || row >= grid.size() || col < 0 || col >= (grid.at(0)).size())     //check whether out of boundary
            return;
        
        if ( (grid.at(row)).at(col) == 1)
        {
            (grid.at(row)).at(col) = 0;      //mark the island as visited
            dfs(grid, row - 1, col);    //up
            dfs(grid, row, col - 1);    //left
            dfs(grid, row, col + 1);    //right
            dfs(grid, row + 1, col);   //down
            count += 1;       
        } 
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        for (int r = 0; r < grid.size(); r++)
        {
            for (int c = 0; c < (grid.at(r)).size(); c++)
            {
                if ( (grid.at(r)).at(c) == 1)
                {
                    dfs(grid, r, c);
                    maxArea = max(maxArea, count);
                    count = 0;
                }
            }
        }
        return maxArea;        
    }
};

int main() {
    Solution sol;

    vector<vector<int>> grid1 = {
        {0,0,1,0,0,0,0,1,0,0,0,0,0},
        {0,0,0,0,0,0,0,1,1,1,0,0,0},
        {0,1,1,0,1,0,0,0,0,0,0,0,0},
        {0,1,0,0,1,1,0,0,1,0,1,0,0},
        {0,1,0,0,1,1,0,0,1,1,1,0,0},
        {0,0,0,0,0,0,0,0,0,0,1,0,0},
        {0,0,0,0,0,0,0,1,1,1,0,0,0},
        {0,0,0,0,0,0,0,1,1,0,0,0,0}
    };

    vector<vector<int>> grid2 = {
        {0,0,0,0,0,0,0,0}
    };

    cout << "Test case 1 (expected 6): " << sol.maxAreaOfIsland(grid1) << endl;

    // Reset state before second call
    sol = Solution();
    cout << "Test case 2 (expected 0): " << sol.maxAreaOfIsland(grid2) << endl;

    return 0;
}