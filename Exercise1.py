# SOLUTION TO THE FIRST QUESTION
def Add(x, y):
    result = x + y
    print("The Answer is = ", result)

Add(2, 2)

# SOLUTION TO THE SECOND QUESTION
# 3x3 matrix
Array1 = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
# 3x3 matrix
Array2 = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
# result is 3x3
def Metrice(X, Y):
    result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
          # iterate through rows of X
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
        # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    for r in result:
        print(r)


Metrice(Array1, Array2)
