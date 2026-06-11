import organizer
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
                    success, moved_files_info = organizer.organize(folder_path)
                    if success:
                        print(messages.SUCCESS_MESSAGE)
                    else:
                        print(messages.ERROR_MESSAGE)
                        
                    utils.display_organization_statistics(moved_files_info)
                    break
                else:
                    print("Invalid path entered.")

        elif choice == "2":
            utils.display_supported_extensions()

        elif choice == "3":
            print(messages.ABOUT_SORTIFY)

        elif choice == "4":
            print(messages.GOODBYE_MESSAGE)
            break

        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()