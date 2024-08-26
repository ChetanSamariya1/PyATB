user_type = input("Enter the user type\n")

match user_type.lower():
    case "admin" | "manager":
        print("Hello, Sir")
    case "guest":
        print("Hello, Guest")
    case _:
        print("Hello, There")