#problem 1
print ("How many marks?")
m = float (input("Enter Marks out of 100:"))

if m >= 85:
    print ("grade of 7")
elif m >= 75 :
    print ("grade 6")
elif m >= 65:
    print ("grade 5")
elif m >= 50:
        print ("grade 4")
else:
    if m < 50:
        print("grade F")

#problem 2

#inputs
basePrice = float (input("How much is the base price?"))
weight = float (input ("What is the weight?:"))
distance = float (input("What is the distance?"))

if distance < 250:
    discount =0         #0%

elif distance < 500:
    discount =0.1       #10 %

elif distance < 1000:
    discount =0.15      #15#

elif distance < 2000:
    discount =0.20      #20%

elif distance < 3000:
    discount =0.35      #35%

else:
    discount = 0.50     #50%

cost = basePrice * weight * distance * (1-discount)

print ("Shipping Cost:", cost)

#problem 3



#sortInterger = sorted ([int1, int2, int3],reverse=False)


# Inputs
int1 = int(input("Integer 1? "))
int2 = int(input("Integer 2? "))
int3 = int(input("Integer 3? "))

# Sorting
min = int1
max = int2

if max< min:
    max, min = min, max

middle = int3

if max <= int3:
    middle = max
    max = int3
elif int3 <= min:
    middle= min

# Output
print("Sorted:", [min, middle, max])



#problem 4

baseWageRate = 36.25
normalWorkHours = 37
overtimeRate= 1.5
bonusPerCar = 200
carsNeededForBonus= 5

hoursWorked= float (input("How many hours did you work?"))
numCarsSold= int (input("Total number of cars sold this week?"))

if hoursWorked <= normalWorkHours:
    regularPay = hoursWorked * baseWageRate
else:
    regularPay = normalWorkHours * baseWageRate

if hoursWorked > normalWorkHours:
    overtimeHours= hoursWorked - normalWorkHours
    overtimePay = overtimeHours * overtimeRate * baseWageRate
else:
    overtimePay=0

bonus =  (numCarsSold - carsNeededForBonus) * bonusPerCar

totalSalary = regularPay+overtimePay+bonus

print (totalSalary)