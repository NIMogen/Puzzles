

"""
Given an MxN matrix, return the a list of the elements of the 
matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Matrix elements are guranteed to be < 100
"""
PASSED = 101


def enspiral_matrix(matrix):
    """
    Define four functions that call eachother in spiral order until they reach a base case, 
    where the starting coordinates for the function call are already set to PASSED.
    This could alternatively be done with a single function that uses several loops and conditionals,
    but I think this is a bit more explicit and form-fitting.
    Each of these functions only iterates through a single row or column.
    """
    return_list = []
    def right(row_i, col_i):
        while col_i != len(matrix[row_i]):
            if matrix[row_i][col_i] == PASSED:
                break
            return_list.append(matrix[row_i][col_i])
            matrix[row_i][col_i] = PASSED
            col_i += 1

        row_i += 1
        col_i -= 1
        down(row_i, col_i)
        
    def left(row_i, col_i):
        while col_i >= 0:
            if matrix[row_i][col_i] == PASSED:
                break
            return_list.append(matrix[row_i][col_i])
            matrix[row_i][col_i] = PASSED
            col_i -= 1
            
            
        col_i += 1
        row_i -= 1
        up(row_i, col_i)
        
    def down(row_i, col_i):
        if matrix[row_i][col_i] == PASSED:
            return

        while row_i != len(matrix):
            if matrix[row_i][col_i] == PASSED:
                break
            return_list.append(matrix[row_i][col_i])
            matrix[row_i][col_i] = PASSED
            row_i += 1

        row_i -= 1
        col_i -= 1
        left(row_i, col_i)
        
    def up(row_i, col_i):
        if matrix[row_i][col_i] == PASSED:
            return
        
        while row_i >= 0:
            if matrix[row_i][col_i] == PASSED:
                break
            return_list.append(matrix[row_i][col_i])
            matrix[row_i][col_i] = PASSED
            row_i -= 1
            
        row_i += 1
        col_i += 1
        right(row_i, col_i)
        
    right(0, 0)
    return return_list


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [1, 2, 3, 4],
              [4, 5, 7, 8]]
    
    matrix2 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    [print(i) for i in enspiral_matrix(matrix)]
    print("----------------")
    [print(i) for i in enspiral_matrix(matrix2)]
