grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

for i in range(len(grades)):
    grades[i] = sum(grades[i])/len(grades[i])

#grades[0] = sum(grades[0])/len(grades[0])
#grades[1] = sum(grades[1])/len(grades[1])

grade = dict(zip(students, grades))
print(grade)
