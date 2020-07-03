def get_input_2():
    a, b = input("\nEnter size of first matrix: ").split()
    print("Enter first Matrix: ")
    matrix1 = []
    for i in range(int(a)):
        row = list(map(float, input().split()))
        matrix1.append(row)

    m, n = input("Enter size of second matrix: ").split()
    print("Enter second Matrix: ")
    matrix2 = []
    for i in range(int(m)):
        row = list(map(float, input().split()))
        matrix2.append(row)
    return matrix1, matrix2

def get_input_1():
    a, b = input("\nEnter size of first matrix: ").split()
    print("Enter Matrix: ")
    matrix1 = []
    for i in range(int(a)):
        row = list(map(float, input().split()))
        matrix1.append(row)
    return matrix1
   
   
def scalar_mul():
    matrix1 = get_input_1()
    n = int(input("Enter the number : "))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix1[i][j] *= n
            print(matrix1[i][j], end="    ")
        print()
        
def addition(matrix1, matrix2):
    result =[[0 for col in range(len(matrix1[0]))]for row in range(len(matrix1))]
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]) :
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        return result    
    else:
        return None
        
def matrix_mul(matrix1, matrix2):
    result =[[0 for col in range(len(matrix2[0]))]for row in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            result[i][j]=0
            for k in range(len(matrix1[0])):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
    return result
        
def result_show(result):
    print("The result is:")
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(round(result[i][j], 2), end="    ")
        print()

def main_diagonal(A):
    result =[[0 for col in range(len(A))]for row in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[j][i]
    result_show(result)
    
def side_diagonal(A):
    result =[[0 for col in range(len(A))]for row in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[j][i]
    for row in result:
        row.reverse()
    result.reverse()
    result_show(result)

def vertical_line(A):
    for row in A:
        row.reverse()
    result_show(A)
    
def horizontal_line(A):
    A.reverse()
    result_show(A)

def transpose():
    print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice = int(input("Your choice: "))
    matrix1 = get_input_1()
    
    if choice == 1:
        main_diagonal(matrix1)
    elif choice == 2:
        side_diagonal(matrix1)
    elif choice == 3:
        vertical_line(matrix1)
    elif choice == 4:
        horizontal_line(matrix1)

def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 1:
        return int(A[0][0])
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = list.copy(A)
        As = As[1:] 
        height = len(As)
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det 
 
    return total

       
def determinant():
    matrix1 = get_input_1()
    det = determinant_recursive(matrix1)        
    print("The result is:\n", det)
    
def invert_matrix(A, tol=None):
    n = len(A)
    AM = list.copy(A)
    I =[[1 if col==row else 0 for col in range(n)]for row in range(n)]
    IM = list.copy(I)
    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(n): 
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler

        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = AM[i][fd]
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM
    
def inverse():
    matrix1 = get_input_1()
    inverse = invert_matrix(matrix1)
    result_show(inverse)

    





    
print("Numeric Matrix Processor")                   
while True:
    print("""\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices
4. Transpose matrix\n5. Calculate a determinant\n6. Calculate Inverse\n0. Exit""")
    choice = int(input("Your choice: "))
    if choice == 1:
        matrix1, matrix2 = get_input_2()
        result = addition(matrix1, matrix2)
        if result != None:
            result_show(result)
        else:
            print("The operation cannot be performed.")
    elif choice == 2:
        scalar_mul()
    elif choice == 3:
        matrix1, matrix2 = get_input_2()
        result = matrix_mul(matrix1, matrix2)
        result_show(result)
    elif choice == 4:
        transpose()
    elif choice == 5:
        determinant()
    elif choice == 6:
        inverse()
    elif choice == 0:
        break
    else:
        print("Invalid Choice.")
        
