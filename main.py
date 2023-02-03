def main():
    while True:
        print("store a password: ")
        print("get a password: ")
        print("quit program: ")

        option = int(input("Enter your choice: "))

        if option == 1:
            category = input("Enter a category for the password: ")
            website = input("Enter a website(or app) for the password: ")
            username = input("Enter the nickname: ")
            password = input("Enter the password: ")
            filename = category + "_" + website + ".txt"

            with open(filename, 'w') as f:
                f.write("website: " + website + "\n")
                f.write("username: " + username + "\n")
                f.write("password: " + password + "\n")
