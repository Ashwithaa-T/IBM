username = ("Ramesh@123","Siri#134","Alex@156","Lalitha123","RaviRaj17")
password = (2007,4567,8907,1278,1901)
username_input = input("Enter the username ")
logic = False
for i in range(len(username)):
    if username_input == username[i] :
        index = i
        logic = True

if logic:
    print(f" For the username {username_input} the password is {password[index]}")
else:
    print("Enter valid user name")

