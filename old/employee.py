class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#emp_1 = Employee('Corey', 'Schafer', 50000)
#emp_2 = Employee('Test', 'Employee', 60000)

qty = int(input("Please input the number of empoyees at your company: "))
#emp = {}

for i in range (qty):
    emp[i] = Employee(first = input("Employee {} first name: ".format(i)), last = input("Employee {} last name: ".format(i)), pay = input("Employee {} salary: ".format(i)))
    #print (emp[i].fullname(), " ", emp[i].pay())

#print (emp_1.fullname())
