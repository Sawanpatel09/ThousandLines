'''class Person:
    name = "patel"
    #@classmethod
    def class1(cls,name):
        cls.name = name

n1 = Person()
n1.class1("sawan")

print(Person.name)
print(n1.name)
'''




'''n = 6
for i in range(n-1,-1,-1):
    for j in range(0,n):
        if i <= j:
            print("#",end="")
        else:
            print(" ",end="")
    print()'''














'''class Employee:
    def __init__(self,role,department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showdetails(self):
        print("the role is",self.role,"and departmet",self.department," and salary is",self.salary)
class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        super().__init__(role,department,salary)
        self.name = name
        self.age = age
    #@property
    def print_name(self):
        print(self.name)
'''






'''class Circle:
    def __init__(self,radius):
        self.radius = radius
    def circumstance(self):
        return 2 *(22/7) * self.radius

c1 = Circle(4)
print(c1.circumstance())'''





'''class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self, c2):
        newreal = self.real + c2.real
        newimg = self.img + c2.img
        return Complex(newreal,newimg)


c1 = Complex(2,3)
c1.shownumber()
c2 = Complex(5,2)
c2.shownumber()
c3 = c1 + c2
c3.shownumber()'''













'''@classmethod
@staticmethod
@property
@isinstance()
'''






'''class Person:
    def __init__(self,name,roll_no):
        self.__name = name
        self.roll_no = roll_no
    def __print_roll(self):
        print(self.roll_no)
    def print_name(self):
        print(self.__name)
        self.__print_roll()
p1 = Person("sawan",89)
(p1.print_name())'''




'''class Accounnt:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance
    def credit(self,current_amount):
        self.balance = self.balance + current_amount
    def debit(self,current_debit):
        self.balance = self.balance - current_debit
    def current_balance(self):
        print("this is your current balance",self.balance)
a1 = Accounnt(3303511,30000)
a1.credit(500)
a1.debit(300)
a1.current_balance()'''






'''class Student:
    def __init__(self,name):
        self.name = name
        self.list1 = []
    def get_average(self):
        sum1 = 0
        for i in self.list1:
            sum1 = sum1 + i
        return sum1/ len(self.list1)

s1 = Student("karan")
s1.list1 = [7,7,7]
print(s1.get_average())'''








'''class Student:
    color = "black"
    def __init__(self,color,gender):
        self.color = color
        self.gender = gender

g1 = "male"
s1 = Student(c1, g1)
print(s1.color,s1.gender)
'''






'''def for_yeild():
    for i in range(5):
        return i     #############################3yeild ======

obj = for_yeild()
for i in range(5):
    print((obj))'''



'''class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
        self.contact = 776778
    def toshowname(self, name):
        self.name = name
        print(self.name)


e1 = Employee("gabbar", 89)
print(e1.toshowname())'''








'''def add(datatype, *args):
    if datatype == "int":
        answer = 0
    if datatype == "str" :
        answer = ''

    for x in args:
        answer = answer + x

    print(answer)


add('int', 3, 8)
add('str', "hello", " name")
'''


'''class Car:
    def __init__(self, brand, model, year, specialization):
        self.brand = brand
        self.model = model
        self.year = year
        self.specialization = specialization
        self.list1 = []
        self.is_electric = False
    def tobrand(self):
        return self.brand
       # if self.brand == "mahindra":
        #    self.list1.append(self.brand)
    def toshowbrand(self):
        return self.brand

    def iselectric(self):
        if self.specialization == "electric":
            self.is_electric = True
    def totrueiselectric(self):
        return self.is_electric

class Electriccar(Car):
    def __init__(self, brand, year,model, specialization, batterysize):
        super().__init__(brand, model, year, specialization)
        self.batterysize = batterysize
        self.specialization = specialization
        self.list2 = []
    def iftrueelectric(self):
        if self.is_electric == True:
            self.list2.append(self.is_electric) #specialization





#mycar1 = Car("mahindra","xuv","2016","petrol")
#mycar2 = Car("tata","harrier", "2019","electric")
#mycar1.tobrand()
#print(mycar1.toshowbrand())
#mycar2.iselectric()
#print(mycar2.totrueiselectric())

mycar1 = Electriccar("tata","harrier", "2019","electric", "674")
print(mycar1.toshowbrand())
#myCar6 =
'''

