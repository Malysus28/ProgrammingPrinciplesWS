

class Employee:
    def __init__(self, first, last, amtPay):
        self.fname = first
        self.lname = last
        self.pay = amtPay
        self.email = first + '.' + last + '@gmail.com'
    def fullname(self):
        return '{} {} '.format (self.fname , self.lname)

    def get_pay (self):
        return self.pay
class International_Emp:
    def __init__(self, first,last,amtpay,nationality):
        Employee.__init__(self,first, last, amtpay)
        self.nationality = nationality


emp1 = Employee ('Cory' , 'Milton' , '800')
emp2 = Employee ('Tory' , 'Deal' , '9000')
emp3 = International_Emp ('alice' , 'ale' , '9000', 'African')

print (emp1.get_pay())

print (emp1.fullname())

print (emp1.fname)

print (emp3.nationality)