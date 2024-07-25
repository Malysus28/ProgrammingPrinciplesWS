def RowAverage(matrix):
    ResList = []    for row in matrix:
        ResList.append(float(sum(row) / len(row)))
    return ResList

def ColAverage(matrix):
    ResList = []
    for j in range(len(matrix[0])):
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
        ResList.append(float(col_sum / len(matrix)))
    return ResList

st1 = [int(x) for x in input("Student 1 (courses 1-4): ").split()]
st2 = [int(x) for x in input("Student 2 (courses 1-4): ").split()]
st3 = [int(x) for x in input("Student 3 (courses 1-4): ").split()]
st4 = [int(x) for x in input("Student 4 (courses 1-4): ").split()]
st5 = [int(x) for x in input("Student 5 (courses 1-4): ").split()]

AllStudentMarks = [st1, st2, st3, st4, st5]

StudentAverages = RowAverage(AllStudentMarks)
max_average = max(StudentAverages)

print("The highest average mark of students:", max_average)

ColumnAverages = ColAverage(AllStudentMarks)
max_column_average = max(ColumnAverages)

print("The highest average mark of courses:", max_column_average)
