from openpyxl import *
class Register:
    def user_register(self):
        print("****Create new Account*****\n")
        name=input("enter the name")
        email=input("enter the email")
        password = input("enter the password")
        phonenumber=int(input("enter the phone number"))
        age=int(input("enter the age"))
        file = "User.xlsx"
        wb = load_workbook(file)
        ws = wb['Sheet1']
        li=[name,email,password,phonenumber,age]
        final = []
        i = -1
        for row in ws:
            l = []
            for col in row:
                l.append(col.value)
            final.append(l)
            i += 1
        final.append(li)
        #print(final)
        ws.insert_rows(i)

        i = 0
        for row in ws:
            j = 0
            for index, col in enumerate(row):
                col.value = final[i][j]
                j += 1
            i += 1
        wb.save("User.xlsx")