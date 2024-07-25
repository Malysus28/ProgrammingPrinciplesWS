#problem 2
#python list comprehension

def sumList(list):
    if len (list) == 1:
        return list [0]
    else:
        return list [0] +list [-1]

list1 = [int (x) for x in input ("Enter list 1 :").split()]
list2 = [int (x) for x in input ("Enter list 2 :").split()]

sum1 = sumList(list1)   #call function
sum2 = sumList(list2)


if sum1 != sum2:
    print(max(sum1, sum2))
else:
    print ("The sum of two lists are the same ")