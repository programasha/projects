d = {}
while True:
    action = input("What do you want to do?(add, search, delete, edit)")
    name = input("Write the name")
    if action == "add":
        num = input("Write the number")
        if name in d:
            ans = input("Do you want to change?")
            if ans == "no":
                name = name + "*"
        d[name] = num
        print(d)
    elif action == "search":
        if name in d:
            print(d[name])
        else:
            print("NO")
    elif action == "delete":
        if name in d:
            del d[name]
        print(d)
    elif action == "edit":
        ans = input("What do you want to change?")
        if name in d:
            if ans == "name":
                num = d[name]
                del d[name]
                name = input("Write new name")
                d[name] = num
            elif ans == "number":
                num = input("Write new number")
                d[name] = num
            print(d)
    else:
        print("Incorrect input. Try again.")
    ans = input("Do you want to exit? (YES/NO)")
    if ans == "YES":
        break

