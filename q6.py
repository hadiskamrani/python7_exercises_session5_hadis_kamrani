count = 0
while True:

    user_name = input("username: ")
    password = input("password: ")
    
    if user_name != "admin" or password != "1234":
        print("password ya username eshtebah ast")
        count=count + 1
        if count>=3:
            print("ghofl shod")
            break
    else:
        print("ba movafaghiyat vared shodid")
        break