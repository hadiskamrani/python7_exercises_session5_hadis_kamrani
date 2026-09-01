for i in range(4):
    user_name = input("username: ")
    password = input("password: ")

    if user_name != "admin" or password != "1234":
        print("password ya username eshtebah ast")
        user_name = input("username: ")
        password = input("password: ")
        print("ghofl shod")
    else:
        print("ba movafaghiyat vared shodid")
