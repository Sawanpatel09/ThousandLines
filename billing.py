'''user_dict = {}

num_entries = int(input("enter the how many items you have"))

for i in range(num_entries):
    key = input("enter name of item: ")
    value = input("enter price of item: ")
    user_dict[key] = value

print("items and their price", user_dict)
list1 =[]

for values in user_dict.values():
    list1.append(values)

sum = 0

for i in list1:
    sum = sum + int(i)
print("the total amount of your billing is this ",sum)'''



'''item1 = []
price1 = []
num_entries = int(input("enter the how many items you have"))
for i in range(num_entries):
    item = input("enter name of item: ")
    price = int(input("enter price of item: "))
    item1.append(item)
    price1.append(price)
sum = 0
for i in price1:
    sum = sum + i
print(sum)'''

'''
sum = 0
while True:
    x = input("enter the item price or  preess q if your billing process complete ")
    if x != "q": 
     sum = sum + int(x)
    else:
        print("thanks for using this and  your amount is ",sum)
        break
    '''

