#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

// Create a function that traverses an MxN matrix, and zeroes out the row and column
// of any element that has the value 0

vector<vector<int>> gen_matrix(int m, int n, vector<tuple<int, int>> zeroes) {
	vector<vector<int>> to_return(m, std::vector<int>(n, 1));
	for (auto pair: zeroes) {
		to_return[get<0>(pair)][get<1>(pair)] = 0;
	}
	
	return to_return;
}

vector<vector<int>> zero_out(vector<vector<int>> matrix) {
	vector<int> skip_col;
	for (auto row = 0; row < matrix.size(); row++) {
		for (auto col = 0; col < matrix[row].size(); col++) {
			if (matrix[row][col] == 0 && find(skip_col.begin(), skip_col.end(), col) == skip_col.end())	{
				skip_col.push_back(col);				
				// Zero out row and column
				for (auto i = 0; i < matrix[row].size(); i++) {
					matrix[row][i] = 0;
				}
				for (auto j = 0; j < matrix.size(); j++) {
					matrix[j][col] = 0;
				}
				// Move onto next row
				break;
			}
		}
	}
	return matrix;
}


int main() {
	vector<tuple<int, int>> z;
	z.push_back(tuple<int, int>{1, 1});
	auto matrix = gen_matrix(12, 10, z);
	for (auto row = 0; row < matrix.size(); row++) {
		for (auto col = 0; col < matrix[row].size(); col++) {
			cout << matrix[row][col];
		}
		cout << endl;
	}
	
	cout << "#######" << endl;

	auto new_matrix = zero_out(matrix);
	for (auto row = 0; row < new_matrix.size(); row++) {
		for (auto col = 0; col < new_matrix[row].size(); col++) {
			cout << new_matrix[row][col];
		}
		cout << endl;
	}

	return 0;
}
