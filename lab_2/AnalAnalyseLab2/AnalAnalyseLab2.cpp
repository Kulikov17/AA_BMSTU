#include <iostream>

using namespace std;


using namespace std;

int main()
{
	int n = 4;										//1
	int* arr = new int[n];		                    //2
	int left = 0;									//3
	int right = n - 1;								//4
	for (int i = 0; i < n; i++)						//5
	{
		arr[i] = n - i;								//6
	}
	for (int i = 0; i < n; i++)
		cout << arr[i];
	cout << endl;
	while (left <= right)							//7
	{
		for (int i = left; i < right; i++)			//8
		{
			if (arr[i] > arr[i + 1])				//9
			{
				int tmp = arr[i];					//10
				arr[i] = arr[i + 1];				//11
				arr[i + 1] = tmp;					//12
				cout << "if" << endl;
			}
		}
		cout << "right" << endl;
		for (int i = 0; i < n; i++)
			cout << arr[i];
		cout << endl;
		right--;									//13
	
		for (int j = right; j >= left; j--)			//14
		{
			if (arr[j - 1] > arr[j])				//15
			{
				int tmp = arr[j];					//16
				arr[j] = arr[j - 1];				//17
				arr[j - 1] = tmp;					//18
				cout << "if" << endl;
			}
		}
		left++;										//19
		cout << "left" << endl;
		for (int i = 0; i < n; i++)
			cout << arr[i];
		cout << endl;
		cout << "cicle"<<endl;
	}
	delete [] arr;									//20

	return 0;
}

/*int main(int argc, char* argv[])
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
}*/