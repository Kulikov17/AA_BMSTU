#include "lab4.h"

bool compare_matrix(const vector<vector<int>>& A, const vector<vector<int>>& B)
{
	if (A.size() != B.size())
		return false;
	if (A[0].size() != B[0].size())
		return false;
	for (int i = 0; i < (int)A.size(); i++)
	{
		for (int j = 0; j < (int)A[0].size(); j++)
		{
			if (A[i][j] != B[i][j])
			{
				return false;
			}
		}
	}
	return true;
}

void testing()
{
	vector<vector<int>> C;
	vector<vector<int>> A =      { {1, 4, 7},
								   {2, 5, 8},
								   {3, 6, 9} };
	vector<vector<int>> B =      { {1, 0, 0},
								   {0, 1, 0},
								   {0, 0, 1} };
	int flag = 0;
	vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
	if (compare_matrix(A, C))
		flag++;
	threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
	if (compare_matrix(A, C))
		flag++;
	if (flag == 2)
		printf("Test multiplication matrix and identity matrix: OK\n");
	else
		printf("Test multiplication matrix and identity matrix: ERROR\n");
	A = { {2, 6},
		  {7, 8},
		  {9, 10} };
	B = { {1, 2, 3, 4},
		  {5, 6, 7, 8}};
	vector<vector<int>> C1 = { {32,	40,	48,	56},
							   {47,	62,	77,	92},
							   {59,	78,	97,	116} };
	flag = 0;
	vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
	if (compare_matrix(C1, C))
		flag++;
	threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
	if (compare_matrix(C1, C))
		flag++;
	if (flag == 2)
		printf("Test multiplication matrix 3x2 and matrix 2x4: OK\n");
	else
		printf("Test multiplication matrix 3x2 and matrix 2x4: ERROR\n");
}

/*int main()
{
	testing();
	return OK;
}*/