import Admin
import Register
import User

class Base_Class:

    def main(self):
        while True:
            print("\t\t_________________________________________")
            print("\t\t\t -------Main Screen-------")
            print("\t\t_________________________________________")
            print("\t\t\t1-> Admin")
            print("\t\t\t2-> RegisterUser")
            print("\t\t\t3-> Userlogin")
            print("\t\t\t4-> Exit")
            choice1 = int(input("\t\t\tEnter your choice(1/2/3/4):-"))
            if choice1 == 1:
                am = Admin.Admin()
                am.adminscreen()
            elif choice1 == 2:
                r=Register.Register()
                r.user_register()
            elif choice1 == 3:
                u=User.User()
                u.user_login()
            elif choice1 == 4:
                exit()
            else:
               print("Invalid input")


Bs = Base_Class()
Bs.main()