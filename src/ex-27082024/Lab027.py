browser_name=input("Enter Name")
browser_name=browser_name.lower()
match browser_name:
    case  "chrome":
     print("Its chrome")
    case  "Firefox":
        print("Its firefox")
    case _:
        print("No browser found")