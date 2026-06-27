'''class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def getbrand(self):
        return self.__brand
class Electriccar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize
        self.list1 = []
        self.my_dict = { }
    def saveinfo(self):
        #self.list1 = []
        self.list1.append(self.model)
    def returnlist(self):
        return self.list1

    def brandandmodelindict(self):
        self.my_dict.update({self.getbrand():self.model})

    def return_my_dict(self):
        return self.my_dict


mycar1 = Car("tata","harrier")
mycar3  = Car("mahindra","scorpio")
print(mycar1.get())
mycar2 = Electriccar(mycar1.get(),"dsgg","78267")
print(mycar2.get())
mycar2 = Electriccar(mycar1.getbrand(),mycar1.model,"463776")
mycar4 = Electriccar(mycar3.getbrand(),mycar3.model,"463776")
#mycar2.saveinfo()
mycar2.saveinfo()
mycar4.saveinfo()
mycar2.brandandmodelindict()
mycar4.brandandmodelindict()
print(mycar2.return_my_dict(),mycar4.return_my_dict())
'''


'''def fibo(n):
    list1 = [1]
    if n <= 2:
        if n == 2:
            list1.append(1)
            return list1

    else:
        f1 = 1
        f2  = 1
        for i in range(2, n):
            res = f1 + f2
            f1 = f2
            f2 = res
            list1.append(res)
    

    return list1

print(fibo(1))
'''



'''n = 50
for i in range(2,n):
    if i == 2:
        print(i)
        continue
    for j in range(3,n):
        if i%j == 0:
            break
    print(i)'''





'''n = 38
for i in range(2,n):
    is_prime = True
    if i == 2:
        is_prime = True
    for j in range(3,i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
'''








'''n = 40
for i in range(1,n+1):
    if n/i == i:
        print("this number is square")

n = 36
square_root = int(n**0.5)
if n % square_root == 0:
    print("this number is prime")

'''




'''matrix1 = [[1, 2],
           [3, 4]]
matrix2 = [[5, 6],
           [7, 8]]
result = [[0,0],
          [0,0]]
for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        #break
print(result)'''


'''matrix1 = [[1, 2, 6],
           [3, 4, 7],
           [8, 3, 6]]
matrix2 = [[5, 6, 9],
           [7, 8, 10],
           [5, 6, 7]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j]+matrix2[i][j]
print(result)
'''









'''dict1 = {x: x**2 for x in range(1,6)}
print(dict1)
dict2 = {y: y**3 for y in range(1,9)}
print(dict2)
'''
'''person = {'name': 'Alice', 'city': 'London'}
person.pop('age',None)
print(person)'''
'''original = {'a': 1, 'b': 2, 'c': 3}
inverted_dictionary = {value: key for key,value in original.items()}
print(inverted_dictionary)
'''
'''original = {'a': 1, 'b': 2, 'c': 3}
inverted_dictionary = {}
for key,value in original.items():
    inverted_dictionary.update({value:key})
print(inverted_dictionary)
'''
'''data = {'apple': 3, 'banana': 5, 'orange': 2}
invert_dict = {}
for key, value in data.items():
    invert_dict.update({value:key})
print(invert_dict)'''

'''data = {'apple': 3, 'banana': 5, 'orange': 2}
invert_dict = {}
n = len(data)
list1 = list(data.items())
# print(list1)
for i in range(n):
    key,value = list1[i]
    invert_dict.update({value:key})
print(invert_dict)'''

'''data = {'apple': 3, 'banana': 5, 'orange': 2}
n = len(data)
invert_dict = {}
list1 = list(data.items())
for i in range(n):
    key,value = list1[i]
    invert_dict[value] = key
print(invert_dict)
'''
'''data = {'apple': 3, 'banana': 5, 'orange': 2}
n = len(data)
list1 = list(data.items())
count = 0
for i in range(n):
    key, value = list1[i]
    count = count + value
print(count)'''

'''scores = {'John': 75, 'Emily': 85, 'Anna': 92, 'Mike': 60}
n = len(scores)
max = 0
list1 = list(scores.items())
for i in range(n):
    key,values = list1[i]
    # print(values)
    if values > max:
        max = values
print(max)
'''




'''dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}'''
'''nested_dict = {'dict1': {'a': 1}, 'dict2': {'b': 2}}
print(nested_dict['dict1']['a'])'''

'''my_dict = {'name':{'a': 1,'c': 5},'city':{'b':2,'d': 5}}
print(my_dict['city']['d'])
'''
'''numbers = [1, 2, 2, 3, 4, 4, 4, 5]
dict1 = {}
for i in numbers:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1
print(dict1)
'''


'''data = {'a': 10, 'b': 5, 'c': 8}
sorted_data = dict(sorted(data.items(), key = lambda item:item[1]))
print(sorted_data)
'''








'''list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = list1 + list2 #[1, 3, 5, 2, 4, 6]
for i in range(len(list3)):
    for j in range(len(list3)):
    '''
'''list1 = [1, 3, 5]
list2 = [2, 4, 6]'''

'''list3 = [1, 3, 5, 2, 4, 6]
for i in range(len(list3)):
    for j in range(0, len(list3) - i - 1):
        if list3[j] > list3[j + 1]:
            list3[j], list3[j + 1] = list3[j + 1], list3[j]
                  # Print the sorted list
print(list3)'''

'''list1 = [1, 2, 3, 4, 2, 5, 3]
list2 = []
n = len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i] == list1[j]:
            list2.append(list1[i])
print(list2)

'''





'''def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return "this is not prime"
        else:
            return "yeah its prime"

print(prime(8))
'''
'''for i in range(2,50):
    is_prime= True
    if i == 2:
        is_prime = True
    for j in range(3,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)'''


'''for i in range(2,50):
    if i == 2:
        print(i)
        continue
    for j in range(3,i):
        if i % j == 0:
            break
    else:
        print(i)
'''







'''str1 = "OpenAI"
str2 = "iouaeIOUAE"
str3 = ""
count = 0
for i in str1:
    if i in str2:
        count = count + 1
        str3 = str3 + i
print(count,str3)
'''


















'''arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
res = -float('inf')
list1 = []
for i in range(n):
    list2 = []
    sum = 0
    for j in range(i,n):
        sum = sum+arr[j]
        list2.append(arr[j])
        if sum > res:
            res = sum
            list1 = list2[:]
print(res,list1)
'''



'''def tocheckprime(n):
    for i in range(2, n):
        if n % i == 0:
            return "the number is not prime"
            pass
        else:
            if i == n-1:
                return "the number is prime"


print(tocheckprime(7))
'''

'''str1 = "madam"
str2  = ""
n = len(str1)-1
i = 0
while n >= 0:
    str2 = str2 + str1[n]
    n = n-1
if str1 == str2:
    print("all good")
else:
    print("not good")
'''
'''str1  = "name"
reverse_string = ""
for i in str1:
    reverse_string= i + reverse_string
if reverse_string == str1:
    print("all are good")
else:
    print("not good")
'''
'''str1 = "name"
str2 = ""
n = len(str1)
for i in range(n-1,-1,-1):
    str2 = str2 +str1[i]
if str1 == str2:
    print("all are good")
else:
    print("not to good")'''















'''str1 = "listen"
str2 = "ient"
list1 = []
for i in range(len(str1)):
    if str1[i] in str2:
        if i == len(str1)-1:
            print("all are good")
    else:
        print("this strings are not anagrams ")
        break

'''










'''list1 = [10, 20, 4,  99]
n = len(list1)
check = 0
for i in range(n):
    if list1[i] > check:
        if i == n-1:
            print(check)
        check = list1[i]'''
'''def  tosecondlarge(list1):
    n = len(list1)
    check = 0
    for i in range(n):
        if list1[i] > check:
            if i == n - 1:
                return check
            check = list1[i]

list1 = [10, 20, 4,  99]
print(tosecondlarge(list1))'''







'''n = 49
for i in range(1, n + 1):
    if n / i == i:
        print("this number is square of this", i)
        break

n = 49
sqrt = int(n ** 0.5)
if sqrt * sqrt == n:
    print("this number is square", sqrt)
'''

'''def square(n):
    sqrt = int(n ** 0.5)
    if sqrt * sqrt == n:
        print("this number is square", sqrt)
    else:
        print("this number is invalid and not an square of any number")
square(34)
def square2(n):
    for i in range(1, n+1):
        if n/i == i:
               print("this number is square of this number",i)

        return print("this not valid square of anny number",n)

square2(34)
'''

'''def square(n):
    sqrt = int(n ** 0.5)
    if sqrt * sqrt == n:
        print("this number is square", sqrt)
    else:
        print("this number is invalid and not an square of any number")
def square2(n):
    square(n)
    print("khdh")
   
square2(34)
'''
'''def polymorphism(a1, a2):
    return a1 * a2
print(polymorphism('a',7))
print(polymorphism(7,7)
    '''


'''def area(radius):
    area = math.pi*radius*radius
    circumference = 2*math.pi*radius
    return area, circumference

a,b = area(3)
print(a,b)'''
'''def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

(print_kwargs(name = "shaktiman",power = "lazer"))
(print_kwargs(name = "shaktiman"))
(print_kwargs(name = "shaktiman",power = "lazer",enemy = "dr. jackel"))
'''
'''def fibo(n):
   
    if n <= 2:
        return 1

    else:
        f1 = 1
        f2 = 1
        for i in range(2,n):
            res = f1 + f2
            f1 = f2
            f2 = res
    return res

print(fibo(10))
'''
'''def chaicode(num):
    def actual(x):
        return x ** num
    return actual
f = chaicode(2)
print(f(3))'''




