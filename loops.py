'''class Employee():
    def __init__(self,role,dprt,salary):
        self.role = role
        self.dprt = dprt
        self.salary = salary
    def showdwtails(self):
        print("role =",self.role)
        print("depa =",self.dprt)
        print("salary =",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Developer","IT","50,000")


engin1 = Engineer("Alice", 28)
'''



















'''class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
c1 = circle(21)
print(c1.area())
print(c1.perimeter())'''




'''class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def shownumber2(self):
        print(self.real, "i -", self.img, "j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newReal,newimg)

    def __sub__(self,num2):
        newReal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newReal,newimg)


num1 = Complex(1,3)
num1.shownumber()

num2 = Complex(4,6)
num2.shownumber()
#num3 = num1+num2
#num3.shownumber()
num3 = num2-num1
num3.shownumber2()'''

#num3 = num1.add(num2)
#num3.shownumber()







'''class Student:
    def __init__(self,phy,chem,math):
        self.physics = phy
        self.chemistry = chem
        self.maths = math
        #self.percentage = str((self.maths + self.physics + self.chemistry)/3)+ "%"
    #def calculatepercentage(self):
        #self.percentage = str((self.maths + self.physics + self.chemistry) / 3) + "%"
    @property
    def percentage(self):
        return str((self.maths + self.physics + self.chemistry) / 3) + "%"

stu1 = Student(67,87,87)
print(stu1.percentage)
stu1.physics = 54
print(stu1.percentage)
'''







'''class Person:
    name = "anonymous"
    @classmethod
    def changename(cls,name):
        cls.name = name



p1 = Person()
p1.changename("rahul kumar")
print(p1.name)
print(Person.name)
'''




'''class BankAccount:
    def __init__(self,balance,):
        self.__balance = balance

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
         self.__balance-= amount
        else:
            print("the amount is invalid")


    def deposit(self,amount):
        if amount > 0:
        #if 0 < amount:
         self.__balance+= amount
        else:
            print("the amount is invalid")

    def checkbalance(self):
        print(self.__balance)

bank1 = BankAccount(5000)
bank1.deposit(100)
bank1.checkbalance()
bank1.withdraw(1000)
bank1.checkbalance()
'''



'''class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
    def information(self):
        print(self.name,self.breed,self.age)

dog1 = Dog("buddy","gdh",3)
dog1.information()'''


'''class Employee:
    company_name = "IT Tech corp"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
emp1 = Employee("jhhdg",787)
print(emp1.name,emp1.salary,emp1.company_name)
emp2 = Employee("alice",6736)
print(emp2.name,emp2.salary,emp2.company_name)

'''



'''class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        self.age = 5
    def bark(self):
       return "woof"

dog1 = Dog("dgg","gsyff")
print(dog1.bark(),dog1.name,dog1.breed,dog1.age)
'''


'''class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_information(self):
        print("this is the  informattion of car",self.make,self.model,self.year)


car1 = Car("mahindra","mmvd",2017)

car1.get_information()'''





'''class A:
    varA = "welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1  = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)'''
'''class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car start...")
    @staticmethod
    def stoped():
        print("car stoped...")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("prius","elecctric")
print(car1.type,car1.name)'''




'''class Person:
    __name = "anonymous"
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()




p1 = Person()
print(p1.welcome())'''


'''class Account:

    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def accountpassword(self):
        print(self.__acc_pass)

acc1 = Account(12345,"yey")
print(acc1.acc_no)
acc1.accountpassword()'''





'''class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("karan")
print(s1.name)
del s1
print(s1.name)'''
'''class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print(self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print(self.get_balance())

    def get_balance(self):
        return "the remaining balnce in account is this",self.balance


a1 = Account(10000,12345)
a1.debit(1000)
a1.credit(500)'''








'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

        sum = 0
    @staticmethod 
    def to_print_hello():
        print("hello")


    def average(self):
        sum = 0
        for val in self.marks:
            sum = sum+val
        print("hi" ,self.name,"your percentage is" ,sum/3,"%")


s1 = Student("tony Stark",[98,87,67])
s1.average()
s1.name = "ironman"
s1.average()
s1.to_print_hello()'''




'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("the  given parameters are")
    def welcome(self):
        print("welecome students", self.name)
    def get_marks(self):
        return print("this are some marks",self.marks)

s1 = Student("karan",67)
print(s1.name,s1.marks)

s1.welcome()
s1.get_marks()
'''




'''with open("practice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    count = 0
    for val in nums:
        if(int(val)%2 == 0):
            count = count+1

print(count)
'''







'''def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find("learning")):
            print("found")
        else:
            print("not foound")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
       while data:
           data = f.readline()
           if (word in data):
              print(line_no)
           line_no = line_no + 1
            
check_for_line()
'''













'''students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eva": 76
}
score = list(students_scores.values())
score.sort(reverse= True)
print(score)

print(score[0],"the topper")
sum = 0
for i in score:
    sum = sum+i

average = sum/len(score)
print(average)
above_average =[]
for i in score:
    if i >=average:
        above_average.append(i)
print(above_average)'''












'''my_dict = {
    "john" : 23,
    "tom" : 10,
    "daire" : 16
}


filterd_key = { }
for key,value in my_dict.items():
    if value > 15:
        filterd_key[key] = value


print(filterd_key)'''


'''my_dict = {
    "yum": 45,
    "tus":78,
    "new":89
}
list1 = []
for key,value in my_dict.items():
    tuple1 = (key,value)
    list1.append(tuple1)
print(list1)'''


'''list = [1,2,2,4]

dictionary = {
    "a" : 2,
    "b" : 3,
    "c" : 4
}
   '''





'''print(dictionary.items())

for key, value in dictionary.items():
    print(key,value)'''



'''dictionary.update({"d":8})
print(dictionary)'''




'''list1 = [(1,2),(1,2),(1,3)]
list3 = [ ]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            list3.append(list1[i])

print(list3)'''


'''list1 = [(1,2,1,2,2),(1,2),(1,1)]
for i in list1:
    for j in range(0,len(i)):
        for k in range(j+1,len(i)):
            if i[j] == i[k]:
                print("present")
                break
'''




















'''list1 = [1,2,3,5,67,4,67]
list2 = [1,2,3,9,10,11,12]

set1 = set(list1)
set2 = set(list2)

set3 = set2.intersection(set1)

list3 = list(set3)
print(list3)'''


'''list1 = [1,2,3,7,5,6]
list2 = [2,1,5,3,1,8]
list3 = []
for i in list1:
    for j in list2:
        if i == j:
         list3.append(i)
print(list3)'''



'''list = [1,3,4,1,3,4,7,8,9,9,9]
list2 = []
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            if list[i] in range(0,5):
                list2.append(list[i])

print(list2)
'''




'''list = ["city","score","city","class","class"]
result = set()

for i in range(0,len(list)):
    if (result.__contains__(list[i])):
        print("the first duplicate",list[i])
        break

       #result.update({list[i]:result.get(list[i])+1})
    else:
        result.update({list[i]})'''


'''list = ["city","city", "gender","home","gender"]
duplicate = []
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            duplicate.append(list[i])
            #duplicate.insert(,i)


print(duplicate)'''






'''list = [10,2,10,3,4,]
#list2 = len(list)
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
          list.pop(i)

          break
print(list)'''






'''def to_check_duplicate(list):
    for i in range(0,len(list)):
      for j in range(i+1,len(list)):
        if list[i] == list[j]:
             return True

    return False

list = [1,2,4,56,3]
print(to_check_duplicate(list))'''







'''list1 = [1,23,1,3,4,1,5,66,6,7,6,7,3]
list2 = set()
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            list2.add(list1[i])


list3 = list(list2)
print(list3)'''







'''list1 = [1,2,3,1,4,4]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            print("the number is duplicate",list1[i])
'''





'''def allprint(list,index):
    if 0>index:
        return


    allprint(list,index-1)
    print(list[index])

list = [1,2,3,4]
allprint(list,3)'''


''' '''

'''def sum_of_natural(n):
    if n == 1:
        return 1
    else:
        return n*sum_of_natural(n-1)

print(sum_of_natural(5))'''




'''def to_check_even_or_odd(n):

    if n%2 == 0:
        return "even"
    else:
        return "odd"


n = int(input("enter a number"))
print(to_check_even_or_odd(n))
'''






'''def rupees_to_usd(n):
    for i in range(1,n+1):
        rupees = i/80
    print(rupees)
    


rupees_to_usd(7)'''








'''def usd_to_rupee(n):
    for i in range(n+1):
      indian_rupee = i*80
    return indian_rupee

print(usd_to_rupee(7))'''








'''def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print(f)
factorial(6)
'''







'''def lenght_of_list(list1):
    print(len(list1))
cities = ["sirra","khandwa","indore","siloda"]
lenght_of_list(cities)'''


'''def print_element_of_list(list1):

    for i in list1:
        print(i,end=" ")
     

list2 = ["city","gender","name"]
print_element_of_list(list2)
'''





'''n = 7
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range((n-1)-i,n-1):
        print("* ",end="")
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(i+1,n):
        print("* ",end="")

    print()'''













'''n = 7
for i in range(1,n):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(n-2, 0, -1):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''






'''n = 7
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(n-i,n):
        print("* ",end="")
    print()'''

'''n = 7
for i in range(1,n):
    for  j in range(1,i+1):
        print("*",end="")
    print()'''









'''scores = [36, 67, 78, 89]
name = ["name", "city","hii", "gender"]
grades = []

for i in range(4):
    grades.append([name[i], scores[i]])

print(grades)'''





'''for i in range(65,91):
    print(chr(i),i)'''
'''n = 7
for i in range(1,n):
    for j in range(1,i):
        print("*", end="")
    for k in range(n-i,n+1):
        print("*",end="")
    print()'''





'''n = int(input("enter a number"))

for i in range(1,n):
    for j in range(1,i+1):
        print(" ",chr((64+j)),end="")
        
    print()'''








'''list1 = [1,2,4,4,5,1]
list2 = set(list1)
#print(list2)
list3 =  list(list2)
#print(list3)
list4 = []

for i in list3:
    if i == 4 or i == 5:
        list4.append(i)

print(list4)'''













'''a = int(input("enter a number"))
b = int(input("enter a number"))
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")'''





'''word1 = (input("enter a 1st name"))
word2 = (input("enter a 2nd name"))
if sorted(word1)==sorted(word2):
    print("the word is anagram")
else:
    print("the word is not anagram")'''








'''n = 153
sum = 0
string1 = str(n)
i = str(1)
while i in string1:
    sum = sum + int(i)**len(string1)
    i = i+1
print(sum)'''

'''n = 153
sum = 0
string1 = str(n)
i = 0

while i < len(string1):
    sum += int(string1[i]) ** len(string1)
    i += 1
if sum == n:
    print("the number is armstrong")
print(sum)'''











'''n = int(input("enter a number"))
if n > 0 :
    print("the number is  positive")
elif n == 0:
    print("the number is zero")
else:
    print("the number is negative")'''





'''n = int(input("enter a number"))
string = str(n)
sum = 0
for i in string:
    sum = sum + int(i)**len(string)
if sum == n:
    print("the number is armstrong",n)
else:
    print("the number is not armstrong")'''







'''n = 3
if n == 0 or n == 1:
    print("the number is not prime", n)
for i in range(2,n):
    if n%i == 0:
        print("the number is not prime ",n)
        break
else:
    print("the number is prime",n)'''








'''string = "name"
string2 = len(string)
reverse_string = ""
for i in range(string2-1,-1,-1):
   reverse_string = reverse_string+string[i]
  

print(reverse_string)
'''






'''n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end= "")
    print()
'''

'''n = 4
#p =int(n/2)
for i in range(0,n):
    for j in range(0,2*n-(i+1)*2):
        print(" ",end="")
        #if n-i == j:

            #m = m -  1
    for k in range(0,2*i+1):
        print("* ",end="")
    print()
#x = int(n/2)
lastStars= 2*n-1
for a in range(0,n-1):
    for b in range(0, 2*(a+1)):
        print(" ",end="")
    #print()
    #print(lastStars)
    for k in range(0,lastStars-(a+1)*2):
        print("* ",end="")

    print()'''










'''def factorial(n):
    list11 = []
    f = 1
    for i in range(1,n+1):
        f = f*i
        list11.append(f)
    return list11
print(factorial(8))'''



'''def fibo(n):
    list1 = [1]

    if n <= 2:
        if (n ==2):
            list1.append(1)
        return list1

    f1 = 1
    f2 = 1
    for i in range(2, n):
        res = f1 + f2
        f1 = f2  #
        f2 = res
        list1.append(res)
    return list1

print(fibo(1))'''

'''def fibo(n):
    if n<=2:
        return 1
    f1 = 1
    f2 = 1
    for  i in  range(2,n):
        res = f1+f2
        f1 = f2
        f2 = res
    return res

print(fibo(5))'''














'''n = 4
for i in range(0,n):
    for j in range(0,2*n-(i+1)*2):
        print(" ",end="")
        #if n-i == j:

            #m = m -  1
    for k in range(0,2*i+1):
        print("* ",end="")
    print()
'''














'''n = 6
 #= 6
for i in range(1,n):
    for j in range(1,n-i+1):
        print(" ",end= "")
        #if n-i == j:

            #m = m -  1
    for k in range(1,i+1):
        print("* ",end="")
    print()'''



'''rows = 6
for i in range(1,rows):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''












'''def fibo(n):
    if n<=2:
        return 1
    f1 = 1
    f2 = 1
    for  i in  range(2,n):
        res = f1+f2
        f1 = f2
        f2 = res
    return res

print(fibo(5))'''












'''def to_check_armstrong(n):
    n = int(input("enter a number"))
    string1 = str(n)
    sum = 0
    for i in string1:
     sum = sum + int(i)**len(string1)
    if  sum == n:
       print("the number is armstrong")
    else:
     print("the number is not armstrong")
to_check_armstrong(153)'''



'''for i in range(5):
    for j in range(5):
        print("*",end="")'''













'''def reverse_string(n):
    reverse_string = ""
    for i in n:
        reverse_string = i+reverse_string
    return reverse_string

print(reverse_string("name"))'''


















'''n = "name"
reverse_string = ""
for i in n:
    reverse_string = i + reverse_string
print(reverse_string)'''







'''def to_check_armstrong(n):
    sum = 0
    string1 = str(n)
    for i in string1:
        sum = sum + int(i)**len(string1)
    if sum == n:
        print("the number is armstrong")
    else:
        print("the number is not armstrong")
to_check_armstrong(15)'''





















'''n = 153
string1 = str(n)
sum = 0
for i in string1:
    sum = sum + int(i)**len(string1)
if sum == n:
    print("the number is armstrong")
'''








'''def to_check_palindrome(str1):
    reverse_string = ""
    for i in str1:
        reverse_string = i + reverse_string
    if reverse_string == str1:
        print("the number is palindrome",str1)
    else:
        print("the number is not  palindrome",str1)
to_check_palindrome("maam")'''





'''str1 = "maab"
reverse_string = ""
for i in str1:
    reverse_string = i + reverse_string
if reverse_string == str1:
    print("the number is palindrome")
else:
    print("the number is not  palindrome")'''





'''n = 5
for i in range(n):
    for j in range(i):
        print("*",end="")'''







'''n = int(input("enter a number"))
count1 = 0
count2 = 0
#if n == 0 or n == 1:
    #count1 = count1 + 1
for i in range(1,n):
    if n % i == 0 or i == 0 or i == 1:
        count1 = count1 + 1
    else:
        count2 = count2+1
print(count1)'''








'''def to_check_prime(n):
    if n == 0 or n == 1:
        print("the number is not prime",n)
    for i in range(2,n):
        if n % i == 0:
            print("the number is not prime",n)
            break
    else:
        print("the number is prime",n)
to_check_prime(9)'''














'''n = int(input("enter a number"))
if n == 0 or n == 1:
 print("the given number is not prime", n)
for i in range(2,n):
    if n % i == 0:
        print("the number is not prime",n)
        break
else:
    print("the number is prime",n)'''






'''def check_even_or_odd(new_series):
    new_series2 = tuple(new_series)
    count1 = 0
    count2 = 0
    for i in new_series2:
        if i%2 == 0:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    print(count1)
    print(count2)
check_even_or_odd((1,2,3,4,5,6,7,8,9))
'''




'''new_series = (1,2,3,4,5,6,7,8,9)
count1 = 0
count2 = 0
for i in new_series:
    if i % 2 == 0:
        count1 = count1+1
    else:
        count2 = count2+1
print(count1, "numbers are my even number")
print(count2, "numbers are my odd numbers")'''









'''def to_check_armstrong(n):
    string1 = str(n)
    lengh_string = len(string1)
    sum = 0
    for i in string1:
        sum = sum + int(i)**lengh_string
    if sum == n:
        print("the number is armstrong",sum)
    else:
        print("the number  is not armstrong")
to_check_armstrong(153)'''








'''n = int(input("enter a number"))
string_n = str(n)
sum = 0
for i in string_n:
    sum = sum + int(i)**len(string_n)
if  sum == n:
    print("the number is armstrong",sum)
else:
    print("the number is not armstrong")
'''












'''def reversed(word):
    reverse_string = ""
    for i in word:
        reverse_string = i + reverse_string
    print(reverse_string)

reversed(str(input("enter a word")))'''





'''word = str(input("enter a word"))
reverse_string = ""
for i in word:
    reverse_string =i + reverse_string
print(reverse_string)'''





'''def is_palinndrome(word):
    reverse_string = ""
    for i in word:
        reverse_string = i +reverse_string
    if word == reverse_string:
        print("the word is palindrome",word)
    else:
        print("the word is not palindrome",reverse_string)
is_palinndrome("name")'''




'''string = "maam"
reverse_string = ""
for i in string:
    reverse_string = i + reverse_string
if string == reverse_string:
    print("the string is palindrome",reverse_string)
else:
    print("the string is not palindrome")'''




'''string1 = "maam"
n = len(string1)
for i in string1:
    if i == string1[n-1]:
        pass



print("string is palindrome")'''

'''string1 = "mhsjgs"
list1 = ""
n = len(string1)
for i in string1:
    for j in string1[n-1]:
        if i == j:
            n = n-1
            list1 = list1 + i
if string1 == list1:
    print("string is palindrome",f"'{string1}'")
else:
    print("this is not palindrome")
'''






'''num = int(input("enter a number"))
temp = num
count = 0
yum = str(temp)
for i in str(temp):
    temp = temp // 10
    count = count + 1
print(count)'''





'''n = "1234"
for i in range(len(n)):
 lenght = len(n)
print(lenght)'''


'''def list_to_number(list1):
    for i in list1:
        print(i)
list_to_number([5,6,7,8])
'''



'''list1 = [1,2,3,5]
for i in list1:
    print(i)
'''



'''def table(n):
    #n = int(input("enter a number"))
    for i in range(1,11):
        print(n*i)
table(6)'''




'''n  = int(input("enter a number"))
for i in range(1,11):
    print(n*i)'''





'''for i in range(1,11):
    if i%2 == 0:
        pass
    else:
        print("the number is odd",i)'''




'''sum = 0
for i in range(1,4):
    sum = sum + i
print(sum)'''




'''for i in range (1,21):
    if i%2  == 0:
        print(i)
    else:
        print("the number is odd")'''





'''for i in range(11):
    print(i)'''