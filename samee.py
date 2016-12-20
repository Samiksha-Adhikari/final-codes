# On start
print("Welcome to prudent Health Care")

users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
    }
}
import time


# approving form
def validate(form):
    if len(form) > 0:
        return False
    return True


# registration
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("---------------------------------")
    print("Account Created Succesfully")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    time.sleep(1)
    print("Account has been created")
    print("---------------------------------")


# login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False


username = {}


# login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return False
    else:
        print("Invalid username or password")
        last()


def last():
    while True:
        print("Options:\n1.Physician\n2.Accountant\n3.Exit\n")
        option = input("> ")
        if option == "1":
            physicianlog()
            while True:
                print("option:\n1.User registration\n2.User Login\n3.Exit\n")
                option = input("> ")
                if option == "1":
                    register()
                elif option == "2":
                    login()
                    while True:
                        print(
                            "Options:\n1.Registration\n2.View Patient\n3.Appointment\n4.Patient Treatment Plan\n5.Exit")
                        option = input("> ")
                        if option == "1":
                            Register()

                        elif option == "2":
                            view()
                        elif option == "3":
                            Appointment()
                        elif option == "4":
                            PTP()

                        elif option == "5":
                            break
                            print("exit")
                        else:
                            print("Wrong choice")
                elif option == "3":
                    break
                    print("Exit")
                else:
                    print("wrong choice")

        elif option == "2":
            accountantlog()
            while True:
                print("option:\n1.User registration\n2.User Login\n3.Exit")
                option = input("> ")
                if option == "1":
                    register()
                elif option == "2":
                    login()
                    while True:
                        print("option:\n1.Invoice ID\n2.View Invoice ID\n3.Exit")
                        option = input("> ")
                        if option == "1":
                            invoiceID()

                        elif option == "2":
                            readinvoiceID()

                        elif option == "3":
                            break
                            print("exit")
                        else:
                            print("wrong choice")
                else:
                    break
                    print("Exit")
        elif option == "3":
            print("Shutting down.....")
            break
        else:
            print(option + " is not an option")


def physicianlog():
    print("")


def accountantlog():
    print("")


# form
def writes(patient_id, first_name, last_name, address, gender, contact, DOB):
    fw = open('data2.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender, contact, DOB))
    fw.close()


def view():
    pid = input("enter ur pid")
    users = open("data2.txt", 'r')

    for each_line in users:
        (patient_id, first_name, last_name, address, gender, contact, DOB) = each_line.split()

        if (patient_id == pid):
            print(patient_id, first_name, last_name, address, gender, contact, DOB)

    users.close()


def cash(pid, name, bill):
    fw = open('data1.txt', "a")
    fw.write("%1s%20s%20s\n" % (pid, name, bill))
    fw.close()


# registration
def Register():
    patient_id = input("Enter patient_id: ")

    first_name = input("Enter your first_name: ")
    last_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    gender = input("Enter your gender: ")
    contact = input("Enter your contact number: ")
    DOB = input("Enter your age: ")
    writes(patient_id, first_name, last_name, address, gender, contact, DOB)
    print("THANK YOU!!!")
    print("\nUser created!\n")


def appiontment(AID, PID, status):
    fw = open('data3.txt', "a")
    fw.write("%1s%20s%20s\n" % (AID, PID, status))
    fw.close()


def Appointment():
    AID = input("Enter Your Appointment ID: ")
    PID = input("Enter Your Patient ID: ")
    status = input("Complete or Appointment: ")
    appiontment(AID, PID, status)


def PTPw(TID, PID, Complain, Treatment):
    fw = open('data3.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (TID, PID, Complain, Treatment))
    fw.close()


def PTP():
    TID = input("Enter Your Treatment ID: ")
    PID = input("Enter Your Patient ID: ")
    Complain = input("Write your complain: ")
    Treatment = input("Given treatment: ")
    PTPw(TID, PID, Complain, Treatment)



    # This is for payment process


def invoice(invoiceID, TreatmentID, bill):
    fw = open('data5.txt', "a")
    fw.write("%1s%20s%20s\n" % (invoiceID, TreatmentID, bill))
    fw.close()


def invoiceID():
    invoiceID = input("Enter your invoiceID:")
    TreatmentID = input("Enter your TreatmentId:")
    bill = input("Please enter the bill amount in Rs.:-")
    print(bill)
    invoice(invoiceID, TreatmentID, bill)
    print("Thank you")


def readinvoiceID():
    Iid = input("enter invoice Id")
    users = open("data5.txt", 'r')

    for each_line in users:
        (invoiceID, TreatmentID, bill) = each_line.split()

        if (invoiceID == Iid):
            print(invoiceID, TreatmentID, bill)
        else:
            print("Patient ID doesn't match")

    users.close()


# ---When you open the program....
print("---------------------------------------")
last()



