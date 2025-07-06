#include <iostream>
#include <vector>

using namespace std;

/* 
    Problem Description:
        - In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into 
        a new one with a different size r x c keeping its original data.
        - You are given an m x n matrix mat and two integers r and c representing the number of rows 
        and the number of columns of the wanted reshaped matrix.
        - The reshaped matrix should be filled with all the elements of the original matrix in the same 
        row-traversing order as they were.
        - If the reshape operation with given parameters is possible and legal, output the new reshaped 
        matrix; Otherwise, output the original matrix.
    
    Constraints:
        m == mat.length
        n == mat[i].length
        1 <= m, n <= 100
        -1000 <= mat[i][j] <= 1000
        1 <= r, c <= 300
*/

vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
    if ( (r * c) != mat.size() * mat.at(0).size() )
    {
        return mat;
    }

    int* visualized = new int[r * c];

    int count = 0;
    for (int i = 0; i < mat.size(); i++)
    {
        for(int j = 0; j < mat.at(i).size(); j++)
        {
            visualized[count] = (mat.at(i)).at(j);
            count++;
        }
    }

    vector<vector<int>> reshaped_mat;
    count = 0;
    for (int i = 0; i < r; i++)
    {
        vector<int> sublist;
        for(int j = 0; j < c; j++)
        {
            sublist.push_back(visualized[count]);
            count++;
        }
        reshaped_mat.push_back(sublist);
    }    
    return reshaped_mat;        
}

int main()
{
    vector<vector<int>> test1 = {
        {1, 2},
        {3, 4}
    };

    cout << "reshaping the test1 vector with row = 1 and col = 4, we get [";
    for(int i = 0; i < matrixReshape(test1, 1, 4).size(); i++)
    {
        cout << "[ ";
        for(int j = 0; j < (matrixReshape(test1, 1, 4).at(i)).size(); j++)
        {
            cout << (matrixReshape(test1, 1, 4).at(i)).at(j) << ", ";
        }
        cout << "], ";
    }
    cout << "] " << endl;


    cout << "reshaping the test1 vector with row = 2 and col = 4, we get [";
    for(int i = 0; i < matrixReshape(test1, 2, 4).size(); i++)
    {
        cout << "[ ";
        for(int j = 0; j < (matrixReshape(test1, 2, 4).at(i)).size(); j++)
        {
            cout << (matrixReshape(test1, 2, 4).at(i)).at(j) << ", ";
        }
        cout << "], ";
    }
    cout << "]" << endl;

    return 0;
}