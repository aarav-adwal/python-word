count = int(input())
list1 = []
for i in range(count):
    user = input().split() #split the user input string into list  e.g user enter insert 0 1 this will save as ['insert',0,1] hence at user[0]=insert and user[1]= 0 and user[2]=1
    if user[0] == 'insert':
        list1.insert(int(user[1]), int(user[2])) # value at user variable which is now a list because of .split funtion at potion 1 and 2 act as postion and value for insert funtion
    elif user[0] == 'remove':
        list1.remove(int(user[1]))
    elif user[0] == 'append':
        list1.append(int(user[1]))
    elif user[0] == "sort":
        list1.sort()
    elif user[0] == 'reverse':
        list1.reverse()
    elif user[0] == 'pop':
        list1.pop()
    elif user[0] == 'print':
        print(list1)
