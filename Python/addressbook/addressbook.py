d = {}
k = 0
while True:
    action = input("Enter command (add, search, delete, edit, exit, print): ")
    if action == "add":
        name = input("Enter the name: ")
        num = input("Enter the number: ")
        if name in d:
            k = k+1
            ans = input("Do you want to change?(yes,no) ")
            if ans == "no":
                name = name + k*"*"
        d[name] = num
    elif action == "search":
        name = input("Enter the name: ")
        p = 0
        for i in d:
            if name in i:
                p = 1
                print(i + " has number " + d[i])
        if p == 0:
            print("Name \"" + name + "\" not found")
    elif action == "delete":
        name = input("Enter the name: ")
        if name in d:
            del d[name]
            print("\"" + name + "\" was deleted ")
        else:
            print("Name \"" + name + "\" not found")
    elif action == "edit":
        name = input("Enter the name: ")
        if name in d:
            ans = input("What do you want to change?(name, number) ")
            if name in d:
                if ans == "name":
                    oldName = name
                    num = d[name]
                    del d[name]
                    name = input("Enter new name: ")
                    d[name] = num
                    print("Name \"" + oldName + "\" was changed to \"" + name + "\"")
                elif ans == "number":
                    num = input("Enter new number: ")
                    d[name] = num
                    print("Name \"" + name + "\" has new number " + num)
                else:
                    print("Incorrect input ")
        else:
            print("Name \"" + name + "\" not found")
    elif action == "exit":
        print("Goodbye!")
        break
    elif action == "print":
        for key in d:
            print(key + " : " + d[key])
    else:
        print("Incorrect input")

