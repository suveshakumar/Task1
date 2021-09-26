import re


def register():
    db = open("database.txt", "a")
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")
    spl = "[@_!#$%^&*()<>?/|}{~:.+-]"
    if re.search("^[^_%#$@*!?][a-zA-z]+[a-zA-Z0-9._#*$%+-]*@[a-zA-Z0-9]+\.[A-Z|a-z]+$", username):
        a = True
        if True in [p.isdigit() for p in password]:
            a = True
            if True in [p.islower() for p in password]:
                a = True
                if True in [p.isupper() for p in password]:
                    a = True
                    if len(password) > 5 and len(password) < 12:
                        a = True
                        if True in [p in spl for p in password]:
                            a = True
                        else:
                            print("Entered Password not met the constraints it should have atleast "+
                                  "one special character,"+
                                  " one digit, one uppercase and one lower case characters. Enter again")
                            register()
                            a = False
                    else:
                        print("Password length should be greater than 5 and less than 12")
                        register()
                        a = False
                else:
                    print("Entered Password not met the constraints it should have atleast one special character, "+
                          "one digit, one uppercase and one lower case characters. Enter again")
                    register()
                    a = False
            else:
                print("Entered Password not met the constraints it should have atleast one special character, "+
                      "one digit, one uppercase and one lower case characters. Enter again")
                register()
                a = False
        else:
            print("Entered Password not met the constraints it should have atleast one special character, "+
                  "one digit, one uppercase and one lower case characters. Enter again")
            register()
            a = False
    else:
        print("Not a valid username")
        register()
        a = False
    if a:
        print("Registered Successfully")
        db.write(username + ", " + password + "\n")


def login():
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")
    db = open("database.txt", "r")
    c = []
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c.append(a)
        d.append(b)
    data = dict(zip(c, d))
    try:
        if data[username]:
            if data[username] == password:
                print("Logined Successfully")
            else:
                inp1 = input("Entered data doesn't exist. Select any one option to proceed" + "\n" +
                             "1. Registration" + "\n" + "2. Forget password - ")
                if inp1 == '1':
                    register()
                elif inp1 == '2':
                    if data[username]:
                        print("Password: " + data[username])
                    else:
                        print("Entered username doesn't exist. Please proceed with the registration")
                        register()
    except:
        print("Entered Username doesn't exist. Please proceed with the registration")
        register()


def home():
    inp = input("Select any one option to proceed:" + "\n" + "1. Registration" + "\n" + "2. Login - ")
    if inp == "1":
        register()
    elif inp == "2":
        login()
    else:
        print("Invalid option selected")
        home()


home()
