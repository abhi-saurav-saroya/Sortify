import organizer
import config
import utils
import messages

def main():
    print(messages.WELCOME_MESSAGE)
    
    while True:
        print(messages.MAIN_MENU)

        choice = input("Enter Choice: ")

        if choice == "1":
            while True:
                folder_path = input("Enter the source folder path you want to organize (main for main menu): ")
                if folder_path == "main":
                    break
                elif utils.is_path_valid(folder_path):
                    organizer.organize(folder_path)
                else:
                    print("Invalid path entered.")

        elif choice == "2":
            utils.display_supported_extensions()

        elif choice == "3":
            print(messages.ABOUT_SORTIFY)

        elif choice == "4":
            print("Thank you for using Sortify!")
            break

        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()