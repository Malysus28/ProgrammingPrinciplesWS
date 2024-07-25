#pt 1

lengthOfPark = float(input ("length of the park (metres):"))
widthOfPark = int(input ("Width of the park (metres):"))
litresPerSquareMetre = float(input ("Litres per square metre: "))


total_litres = lengthOfPark * widthOfPark * litresPerSquareMetre
print ("Litres Required = ", total_litres)


#pt2

numOfHours = float (input ("Number of hours worked per day:"))
numOfDays = int (input("Number of days worked in a week:"))
annualSalary = float (input("Annual Salary:"))

hourly_wage = annualSalary / (52 * numOfHours * numOfDays)  #represents the number of weeks in a year

print ("Hourly Wage = ",hourly_wage)

#pt3

studentsPerClass = 25
bigExamHallCap= 45
smallExamHallCap = 22

numOfBigExamHalls = int (input("How many big exam halls?:"))
numOfSmallExamHalls = int(input("How many small exam halls?:"))

studentCapacity = (numOfBigExamHalls * bigExamHallCap) + (numOfSmallExamHalls * smallExamHallCap)
numOfClasses = studentCapacity // studentsPerClass

print ("Number of Classes=", numOfClasses)
