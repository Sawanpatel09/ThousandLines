'''class A:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def open1(self):
        return self.__age
    def __name1(self):
        return self.name
class B(A):
    def name2(self):
        return self.__name1()
obj = A("Sawan",23)
obj1 = B("Patel",45)
obj._A__name1()'''





'''class Dog:
    def Sound(self):
        print("Bark")
class Cat(Dog):
    def Sound(self):
        print("Meow")

obj = Dog()
obj.Sound()
class Student:
    def add(self,int1,int2):
        return int1 + int2
    def add(self,uu,ii,pp):
        return uu + ii + pp
obj = Student()
print(obj.add("hx","bxh","hx"))'''





'''def compound_intrest(Amount,Annual_interest,n):
    ci = Amount*((1 + Annual_interest/100) ** n) - Amount
    return ci
d = compound_intrest(10000,10,1)
print(d)'''


'''class Mouse:
    Name = "Micky"
    City = "New york"
    def __init__(self,Emp_id,Age):
        self.Emp_id = Emp_id
        self.Age = Age
    def Display(self):
        print("Employee ID",self.Emp_id)
        print("Age",self.Age)
        print("Employee Name",self.Name)

M = Mouse("DRF3452",89)
M.Display()
print(M.City)
print(Mouse.City)'''


'''import re
txt = "Precaution and presentation are important for preparation"
pattern = r"ion\b"
result = re.findall(pattern,txt)
print(result)'''


'''txt = "users.name@example.co.uk"
pattern = "\w+@\w+.\w+.\w+"
result = re.findall(pattern,txt)
print(result)'''



'''import re
txt = "hello world, how are you?"
pattern = "\b[a-z]"
result = re.sub(pattern, lambda m: m.group(0).upper(),txt)
print(result)
print(txt)'''





'''txt = "There is two many    spaces"
pattern = "\s+"
result = re.sub(pattern," ",txt)
print(result)'''




'''txt = "Hello world"
pattern = "\s"
result = re.sub(pattern,"",txt)
print(result)
'''



'''txt = "Python is fun. python is powerful.PYTHON is versatile"
pattern = "PYTHON"
result = re.sub(pattern,"Java",txt,flags=re.IGNORECASE)
print(result)'''






'''txt = "Call us at (123) 456-7890 or (987) 654-3210."
pattern = "\(\d{3}\)\s\d{3}-\d{4}"
result = re.findall(pattern,txt,)
print(result)'''





'''txt = "the years 1999, 2005 and 2023 were significant"
pattern = "\d+"
result = re.findall(pattern,txt)
print(result)
'''





'''txt = "this is #great day for #learning python regex!"
pattern = "#\w+"
result = re.sub(pattern,"",txt)
print(result)'''






'''txt = "Visit https://www.python.org or http://example.com for more info."
pattern = r"https?://[^\s]+"
result = re.findall(pattern,txt)
print(result)'''






# for email searching
'''import re
txt = "Contact us at info@example.com or support@company.org for assistance."
pattern = "\w+@\w+\.\w+"
result = re.findall(pattern,txt)
print(result)'''




# import re
# txt = "my name is sawan@gmail.com"
# a = re.finditer("hh",txt)
# print(a)


# arr = [10,11,12]
# total = 0
# for i in range(len(arr)):
#     total_1 = 0
#     if (i+1) % 2 != 0:
#         count = 0
#         flag = True
#         for j in range(len(arr)):
#             if j > i:
#                 if flag == True:
#                     total = total + total_1
#                     flag = False
#                 total_1 = total_1 - arr[count]
#                 total_1 = total_1 + arr[j]
#                 total += total_1
#                 count = count + 1
#             else:
#                 total_1 = total_1 + arr[j]
#     if i == len(arr) - 1 and total_1 != 0:
#         total = total + total_1
# print(total)




import re
taxt = "my name is sawan"
# x = re.search("^mysawan$",taxt)
# print(x)


















'''try:
    # s = "vxvv"
    # y = 990
    # print(s + y)
    d = 7896
    f = 0
    print(d/f)
except Exception as arg:
    print("There is error",arg)
else:
    print("All are  good")'''








'''
mat = [[1,0,0],[0,0,1],[0,0,0]]
hash1 = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            hash1.append((i,j))
set1 = set()
for i in range(len(hash1)):
    for j in range(i+1,len(hash1)):
        if hash1[i][0] == hash1[j][0] or hash1[i][1] == hash1[j][1]:
            set1.add(hash1[i])
            set1.add(hash1[j])
total = len(hash1) - len(set1)
print(total)'''










'''arr = [2,6,14,10,18]
arr.sort()
diff = ""
list_sample = []
main_list1 = []
for i in range(len(arr)-1):
    if diff == "":
        diff1 = abs(arr[i] - arr[i+1])
        list_sample.append(arr[i])
        diff = diff1
    else:
        diff1 = abs(arr[i] - arr[i+1])
        if diff == diff1:
            list_sample.append(arr[i])
        else:                                  #------------------------------Important--------------- love this algo
            list_sample.append(arr[i])
            if len(main_list1) < len(list_sample):
                main_list1 = list_sample
                list_sample = []
            list_sample = []
            list_sample.append(arr[i])
            diff = diff1
if abs(arr[-1] - arr[-2]) == diff:
    list_sample.append(arr[-1])
if len(main_list1) < len(list_sample):
    main_list1 = list_sample
print(main_list1)'''











'''a = "dcbaa"
str1 = "abcdefghijklmnopqrstuvwxyz"
hash1 = {}
for item in a:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
str2 = ""
for j in range(len(hash1)):
    if str1[j] in hash1:
        for k in range(hash1[str1[j]]):
            str2 = str2 + str1[j]
print(str2)'''






'''str1 = "apple"
hash1 = {}
for item in str1:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
print(hash1)'''



'''str1 = "drf jgkh"
d = str1.replace(" ","")
print(d)
'''


'''str1 = "I love python programming"
str2 = ""
count = 0
for item in str1:
    if item == " ":
        count += 1
        str2 = ""
    else:
        str2 = str2 + item
if str2 != "":
    count += 1
print(count)
'''





'''str1 = "Hello World"
str2 = ""
for item in str1:
    if item.isalpha():
        str2 = str2 + item
print(str2)'''


'''str1 = "Hello World"
count = 0
str2 = "aeiou"
for item in str1:
    if item in str2:
        count += 1
print(count)'''