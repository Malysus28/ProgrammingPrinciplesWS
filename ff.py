
def check_product(a,b,c):
    # Find the largest number
    largest =a
    if b>largest:
        largest=b
    if c >largest:
        largest=c


    smallest =a
    if b <smallest:
        smallest =b
    if c <smallest:
        smallest=c


    if largest *smallest >100:
        return True
    else:
        return False


# Take user input for three numbers
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
c =int(input("Enter third number: "))


result =check_product(a, b, c)
print(result)
