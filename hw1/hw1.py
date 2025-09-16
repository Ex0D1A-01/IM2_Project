# my_list=[]

# row=int(input("enter the number of rows: "))
# col=int(input("enter the number of columns: "))


# for x in range(row):
#     print(f"row: {x+1}")
#     rows=[]
#     for y in range(col):
#          print(f"enter element: {y+1}")
#          rows.append(int(input()))
#     my_list.append(rows)

# print(my_list)


# num = float(input("Enter a number to search: "))
# matches = []


# print("\nThe 2D list is: ")
# for rows in my_list:
#     print(row)
# print()

# for i in range(row):
#     for j in range(col):
#         if my_list[i][j] == num:
#             matches.append((f"Row {i}, Col {j}"))

# if matches:
#     print(f"Number {num} found at " + " and ".join(matches))
# else:
#     print(f"Number {num} not found.")
# print()



#  dict**************** 

# myDict = {}
# rows = int(input("Enter row: "))
# cols = int(input("Enter col: "))
# print()

# for i in range(rows):
#     print(f"Row {i+1}: ")
#     for j in range(cols):
#         key = input(f"Enter key {j+1}: ")
#         value = float(input(f"Enter value {j+1}: "))
#         myDict[key] = value
#     print()

# print("The dictionary is: ")
# for key, value in myDict.items():
#     print(f"{key}: {value}")   
# print()


# value = float(input("Enter a value to search: "))
# found = []

# for key, val in myDict.items():
#     if val == value:
#         found.append(key)

# if found:
#     print(f"Value '{value}' found in keys: {', '.join(found)}")
# else:
#     print(f"Value '{value}' not found.")
    
    
    # tuple**********************************************************************
    
      
myTuple = ()
row = int(input("Enter row: "))
col = int(input("Enter col: "))
print()
for i in range(row):
    print(f"Row {i+1}: ")
    for j in range (col):
        num = float(input(f"Enter number{j+1}: "))
        myTuple += (num,)
    print()

print("The tuple is: ")
for item in myTuple:
    print(item, end = ", ")
print()

#search for a number
num = float(input("Enter a number to search: "))
match = []

for i in range(len(myTuple)):
    if myTuple[i] == num:
        match.append(i)

if match:
    print(f"Number {num} found at indices: {', '.join(map(str, match))}")
else:
    print(f"Number {num} not found.")

