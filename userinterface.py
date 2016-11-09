from database import *


def main():
    c = Database()
    user_input = input("username: ? ")
    user_password = input("password: ? ")
    if user_input in list_of_new_users:
        for row in c.data:
            split_row = row.split(',')
            if user_input == split_row[0]:
                if user_password == split_row[1]:
                    print("Your info: " + "\n"*2 + row + "\n")
                    what_do(c)
    else:
        for row in c.data:
            split_row = row.split(',')
            if user_input == split_row[0]:
                if user_password == split_row[1]:
                    print("Your info: " + "\n"*2 + row + "\n")
                    what_do(c)
                else:
                    main()
            else:
                continue
        main()


def what_do(database):
    what_do_next = input("what would you like to do: (A)dd new user or (L)og out?")
    if what_do_next.lower() == 'a':
        new_username = input("username plz: ")
        for row in database.data:
            split_row = row.split(',')
            if new_username == split_row[0]:
                print("cannot add same user again.")
                what_do(c)
        new_password = input("password plz ")
        new_full_name = input("full name plz ")
        new_phone = input("phone num plz ")
        c.add([new_username, new_password, new_full_name, new_phone])
        list_of_new_users.append(new_username)
        what_do(c)
    else:
        Database._save(c)
        main()

list_of_new_users = []
c = Database()
main()
