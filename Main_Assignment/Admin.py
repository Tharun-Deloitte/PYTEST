class Admin:
    added_movies = []
    movie_timings={}

    def adminscreen(self):
        username = "admin"
        password = "admin123"
        while True:
            Username = input("Enter Your Username:-")
            Password = input("Enter Your Password:-")
            if Username == username and Password == password:
                while True:
                    print("\t\t_________________________________________")
                    print("\t\t\t -------Admin Screen-------")
                    print("\t\t_________________________________________")
                    print("\t\t\t1-> Add Movie info")
                    print("\t\t\t2-> Edit movie info")
                    print("\t\t\t3-> Delete Movie")
                    print("\t\t\t4-> Logout")
                    choice2 = eval(input("\t\t\tEnter your choice(1/2/3/4):-"))
                    if choice2 == 1:
                        self.add_movies()
                    elif choice2 == 2:
                        self.edit_movies()
                    elif choice2 == 3:
                        self.delete_movies()
                    elif choice2 == 4:
                        break
                    # else:
                    #     print("Invalid input")
            else:
                print("Wrong Password.")
                print("1-> Try again")
                print("2-> Quit program")
                choice = eval(input("Enter your choice:-"))
                if choice == 2:
                    print("Quitting the program...")
                    break
                elif choice==1:
                    self.adminscreen()

            break