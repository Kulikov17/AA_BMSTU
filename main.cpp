#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    int arr[9];                                 // 1
    int mtr[3][3];                              // 2 
    int size_arr = 9;                           // 3
    int size_mtr = 3;                           // 4
    arr[0] = 1;                                 // 5
    arr[1] = 1;                                 // 6 
    for (int i = 2; i < size_arr; i++)          // 7
    {
        arr[i] = arr[i - 1] + arr[i - 2];       // 8
    }
    for (int i = 0; i < size_mtr; i++)          // 9
    {               
        for (int j = 0; j < size_mtr; j++)      // 10
        {
            mtr[i][j] = arr[i * size_mtr + j];  // 11
        }

    }

    int tmp;                                    // 12

    for (int i = 0; i < size_mtr; i++)          // 13
    {
        for (int j = 0; j < i; j++)             // 14
        {
            tmp = mtr[j][i];                    // 15
            mtr[j][i] = mtr[i][j];              // 16
            mtr[i][j] = tmp;                    // 17
        }
    }

    return 0;
}