'''h = int(input("please enter diamond's height:"))

for i in range(1, h, 2):
    print(" "*(h//2-i//2), "*"*i)
for i in range(h, 0, -2):
    print(" "*(h//2-i//2), "*"*i)'''






'''n = 7 #int(input("please enter diamond's height:"))

for i in range(n):
    print(" "*(n-i), "*"*(i*2+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i), "*"*(i*2+1))'''








'''n = 7
for i in range(1,n):
    for j in range(1,n-i):
        print("*", end="")
    #for m in range(n,1,-1):
    print()
if n==i+1:
 for k in range(2,n):
    for l in range(2,k+1):
        print("*",end="")
    print()'''



'''n = 7
for j in range(1,n):
 for m in range(j,n):
    print("x",end="")
 print()'''





'''n = 7
for i in range(n,n*2):
    for j in range(5,8):
        print("*",end="")
    print()'''














'''for i in range(1,n+1):
    for j in range(1,i+1):
        print("x",end= "")
    print()
'''



'''def fibo(n):
    if n <= 2:
        return 1
    f1 = 1
    f2 = 1
    for i in range(2,n):
        res = f1 + f2
        f2 = res
        f1 = f2
    return res

print(fibo())'''







'''n = 6
f  = 1
for i in range(1,n+1):
  f = f*i
print(f)'''


'''def fibo(n):
    if n <= 2:
        return 1
    f1 = 1
    f2 = 1
   # return
    for i in range(2,n):
        res = f1+f2
        f2 = res
        f1 = f2
    return res
print(fibo(6))'''



















'''def fibo(n):
    #res = 1;
    if n<=2:
        return 1
    else:
        f1 = 1
        f2 = 1
        for i in range(2, n): # 3
            res = f1 + f2
            f1 =  f2 # f2 = res
            f2 = res # f1 = f2
    #print(res)
    return res

print(fibo(1))
'''










"""def factorial(n):
    f = 1

    for i in range(1,n+1):
        f*=i
    print(f)
factorial(5)"""





'''def singel_line_list(a):
    print(list)
list =[1,2,3,4]
singel_line_list(list)'''




'''def lenght_of_list(a):
    print(len(list1))
list1 = [1,3,4,5]
lenght_of_list(list1)'''




'''def multiply(a,  b=8):
    return a*b
print(multiply(8))'''





'''def average(a,b,c):
    return (a+b+c)/3
average1 = average(1,2,3)
print(average1)
'''


'''def hello1(  ):
    print( "hello")
output = hello1()
print(output)'''





'''def sum1(a,b):
    sum = a+b
    print(sum)
sum1(2,4)
sum1(4,8) '''






'''n = 5
fact =1
for i in range(1,n+1):
    fact*=i
    i+=1
print(fact)'''









'''list1 = [1,2,3,4]
count = 0
addition = 0
while count<len(list1):
    addition = addition + list1[count]
    count+=1
print(addition)'''






'''n = 2
for i in range(1,11):
    print(n*i)'''




'''for i in range(100,0,-1):
    print(i)
'''






'''for i in range(1,100,5):
    print(i )
'''




'''tuple = (1,4,9,16,25,36,49,64,81,100,49,49)
n = 49
index = 0
for i in tuple:
    if i == n:
        print("the n is found",index)

    continue
    
    index+=1
'''








'''list1 = [1,4,9,16,25,36,49,64,81,100]
for i in list1:
    print(i)'''








'''str1 = "nameworld"
for i in str1:
    if i == 'e':
        print("found")
        break
    print(i)
else:
    print("end")'''







'''i = 0
while i <= 20:
    if i % 2 == 0  :
        i+=1
        continue
    print(i)
    i+=1'''






'''i = 1
while i<=5:

     print(i)
    i+=1
'''








'''tuple1 = (1,4,9,16,25,36, 49,64,81,100)
x = 36
count = 0
while count < len(tuple1):
    if tuple1[count] == x:
        print("we found it",[count])
        break
    count+=1
print("loop ended")'''







'''list = [1,4,9,16,25,36, 49,64,81,100]
count = len(list)
x = 25
while count<=len(list):
    if x in list:
        print("yahho we find it")
        break
print("loop ended")'''


'''list = ["name","gender","movies","subject"]
count = 0
while count<=len(list)-1:
    print(list[count])
    count+=1
'''








'''list = [1,4,9,16,25,36,49,64,81,100]
count = 0
while count <=len(list) -1 :
    print(list[count])
    count+=1
print("loop ended")
'''








'''  '''





'''count = 100
while count >= 1:
    print(count)
    count-=1
print("loop ended")'''







'''count = 1
while count<=100:
    print(count)
    count+=1
print("loop ended")
'''







'''i = 5
while i >= 1:
    print(i)
    i = i-1

print("loop ended")
'''








'''count = 1
while count<=5:
    print(count)
    count+=1
print("loop end")'''





'''count = 1
while count<=5:
    print("hello")
    count = count+1
print(count)
'''







'''set1 = {("float",9.0),("int",9)}
print(set1)
'''



'''set1 = set()
intx = int(input("enter a integer value"))
set1.add(intx)
str1 = str(input("enter a str values"))
set1.add(str1)
print(set1)'''







'''marks = {

}
x = int(input("enter marks"))
marks.update({"math":x})
y = int(input("enter marks"))
marks.update({"english":y})
z = int(input("enter marks"))
marks.update({"social":z})

print(marks)
'''




'''dict = {

}
for i in range(1,4):
    subject = str(input("enter subject name"))
    marks = int(input("enter marks"))
    #print(int(subject)+marks)
    dict.update({subject:marks})
print(dict)'''

'''list = ["java","python","c++","javascript","c","python"]
classroom = []
for  item in list:

    if item not in classroom:
     classroom.append(item)
print(classroom)
'''










'''list = ["java","python","c++","javascript","c","python"]
classroom = []
for i in range(len(list)+1):

     for j in range(len(list)+1):

         if i != j:
             classroom.append(i)
         j = j+1'''











'''dict = {}
dict.update({"cat":"animal","table":["a furniture","list of  facts"]})
print(dict)'''







"""set1 = {1,2,3,3,4,5}
set2 = {"name","city","marks"}
set3 = set1.intersection( set2)
print(set3)
"""




'''new_set = {"name","city","gender","marks"}
for i in range(len(new_set)):
    print(new_set.pop()) 
'''







'''new_set = set()
new_set.add(1)
new_set.add(2)
new_set.add(3)
print(new_set)
new_set.remove(2)
print(new_set)
new_set.add((1,2,3))
print(new_set)
new_set.add("name")
print(new_set)
print(len(new_set))
new_set.pop()
print(new_set )'''






'''info = {
    "name" : "ram",
    "subjects" : {
        "math":67,
        "chem":72,
        "physics":72
    },
    "gender": "M"
}
pairs = list(info.items())
print(pairs[0])

info.update({"city":"indore"})
print(info)
info.update({"name":"shyam"})
print(info)
info.update({"subjects":{"math" : 79}})
print(info)'''



'''tuple = ("a","b","c","d","a")
grade_of_a = tuple.count("a")
print(grade_of_a)
list1 = list(tuple)
print(list1)
list1.sort()
print(list1)'''

"""list1 = list(tuple)
print(list1)
sort_list = list1.sort()
print(sort_list)"""




'''list = [1,2,3,2,4]
reverse_list = list[::-1]
if  reverse_list == list:
    print("the list is palindrome")
else:
    print("the list is  not palindrome")
'''

'''list_copy = list.copy()
list.reverse()
print(list)
'''



"""list = [1,3,8,9,12]
list_copy = list.copy()
list.reverse()
if list_copy == list:
    print("the list is palindrome")
else:
    print("the list is not palindrome")
"""



'''movie1 = input("enter  fav1 movie")
movie2 = input("enter fav2 movie")
movie3 = input("enter fav3 movie")
list = []
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)'''


'''tup = (2,4,6,7,1,2,2)
count = tup.count(2)
print(count)
index = tup.index(6)
print(index)'''




'''list = [44,89,23,39]
list.append(71)
print(list)
list.sort()
print(list)
list.remove(39)
print(list)
list.pop(2)
print(list )'''





'''
list = [2,9,6,14,12]
list.sort(reverse = True)
print(list)

list.append(10)
print(list)

list.sort()
print(list)
list.insert(3,"don")
print(list)
list.reverse()
print(list)'''




'''str = "hello"
str[0] = "j"'''





'''a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
d = int(input("enter a number"))
if a>=b and a>=c and a>=d:
    print("a is greater than all")
elif b >= c and b >= d:
    print("b is greater ")
elif c >= d:
    print("c is greater")
else:
    print('d is  greater')'''









'''num1 = int(input("enter a number"))
if num1 % 7 == 0:
    print(f"the {num1} is multiple of seven")
else:
    print(f"the {num1} is not multiple of seven")'''

'''num2 = int(input("enter a nummber"))
if num2 % 8 == 0:
    print("the {} is multiple of eight".format(num2))
else:
    print("the {} the number is not multiple of eight".format(num2))
'''




'''num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
if num1 > num2 and num1 > num3:
    print("num1 is greater than num2 and num3",num1)
elif num2 > num3 and num2 > num1:
    print("num2 is greater than num1 and num3",num2)
elif num3 > num1 and num3 >num2:
    print("num3 is greater than num1 and num3", num3)
else:
    print("inavalid")'''




'''num  = int(input("enter a  number"))
if num % 2 == 0:
    print("the num is even", num)
else:
    print("the num is odd",num)
'''





'''age = int(input("enter age"))
if age >= 18:
    if age > 80:
        print("can not drive with age",age)
    else:
        print("can drive with age",age)
else:
    print("can not drive with age",age)
'''




'''marks = int(input("enter a number"))
if marks >= 90:
    print("A grade",marks)
elif marks < 90 and marks >= 80:
    print("B grade",marks)
elif marks < 80 and  marks >= 70:
    print("C grade", marks)
else:
    print("you are failed")'''


'''marks1 = int(input("enter the marks"))
if  marks1 >= 90: 
    grade = "A"
elif marks1 >= 80 and marks1 < 90:
    grade = "B"
elif marks1 >=70 and marks1 < 80:
    grade = "C"
else:
    grade = "D"
print("the grade of student ",grade)'''







'''first_name = input("enter a name")
print(len(first_name))'''
"""occurence = "the currency of us  is %$"
print(occurence.__contains__("$"))
"""


'''str1 = "hey google"
print(str1.endswith("le"))
print(str1.capitalize())
print(str1.upper())
print(str1.replace("o", "a"))
print(str1.find("l"))
print(str1.count("o "))'''
'''str1 = "apple"
print(str1[-3:-1])'''



'''str = "hello world"
print(str[6:]) '''




'''str1 = "hello"
str2 = "world"
final_str = str1+" "+str2
print(final_str)
print(len(final_str))
print(len(str1))
print(len(str2 ))
print(len(str1)+len(str2))
str1 = "we are doing code\n in python"
print(str1)'''






'''a = int(input("enter a number"))
b = int(input("enter a number"))
camparison = a>=b
print(camparison)
if a>=b:
    print(True)
else:
    print(False)'''




'''a = float(input("enter a 1st number"))
b = float(input("enter a 2nd number"))
average =  (a+b)/2
print(average)'''



'''a = float(input("enter a number"))
area_of_square = a**2
print("the area of square is:", area_of_square)
'''




'''num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
sum = num1 + num2
print(sum)
'''







'''name = input("enter a name: ")
age = int(input("enter a age: "))
marks = float(input("enter a marks: "))
print("welcome",name,"your age is ",age,"and your marks is",marks)'''








'''a = "2"
b = 3
d = int(a)
print(type(d))
sum = d+b
print(sum)'''

'''sal = float(input("enter a number"))
tax = sal*(0.1,0.2) [sal<=50000]
print(tax)
'''


"""age = int(input("enter a age :"))
vote = ("yes","no") [age >= 18]
print(vote)"""





'''age = int(input("enter a age :"))
if age >=18:
    print("yes you are eligible to vote",age)
else:
    print("you are not eligible to vote")
'''








'''food = input("food:")
eat = "yes" if food == "cake" else "no"
print(eat)
food = input("food")
eat = "sweet" if food == "cake" or food == "jalebi" else "no sweet"
print(eat)'''










'''A = int(input("A:"))
G = input("m/f:")
if (A == 5 or A == 4) and G == "m":
    print("fee is 100")
elif( A == 34 or A == 77) and G == "f":
    print("ho jayega bhai")
else:
    print("to krna ")'''





'''marks = int(input("enter a number"))
if marks > 80 and marks < 90:
    print("jj")
elif marks >= 55 and marks <= 60:
    print("uu")
elif marks >= 33 and marks <=40 :
    print("excellent")
else:
    print("tu aisa hi he yaar")'''






'''name = input("color")
if name == "red":
    print(4)
elif name == "white":
    print(9)
elif name == "brown":
    print(10)
else:
    print("all is well")'''




'''def fibo(n):
    list1 = []
    if n<=2:
        return 1
    else:
        f1 = 1
        f2 = 1
        for i in range(2, n): # 3
            res = f1 + f2
            f1 =  f2 # f2 = res
            f2 = res # f1 = f2
            list1.append(res)
    #print(res)
    return list1

print(fibo(7))'''