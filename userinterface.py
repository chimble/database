from database import *


def main():
    c = Database()
    user_input = input("user_nameplz")
    user_password = input("pw plz")
    for row in c.data:
        if user_input in row:
            if user_password in row:
                print("Your info: " + "\n"*2 + row + "\n")
                what_do = input("what would you like to do: (A)dd new user or (L)og out?")
                if what_do.lower() == 'a':
                    new_username = input("username plz: ")
                    for row in c.data:
                        if new_username in row:
                            print("cannot add same user again.")
                            new_username = input("username plz: ")
                            break
                    new_password = input("password plz ")
                    new_full_name = input("full name plz ")
                    new_phone = input("phone num plz ")
                    c.add([new_username, new_password, new_full_name, new_phone])
                    #keep_going = T
                else:
                    main()
            else:
                main()
        else:
            main()






main()
