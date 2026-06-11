import organizer
import utils
import messages
import logger

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
                    logger.log_message(
                        f"Started organization of {folder_path}"
                    )
                    success, moved_files_info = organizer.organize(folder_path)
                    if success:
                        print(messages.SUCCESS_MESSAGE)
                        logger.log_message(
                            "Organization completed successfully"
                        )
                        logger.end_session()
                    else:
                        print(messages.ERROR_MESSAGE)
                        logger.log_message(
                            "Organization failed completely or partially"
                        )
                        logger.end_session()
                        
                    utils.display_organization_statistics(moved_files_info)
                    break
                else:
                    print("Invalid path entered.")
                    logger.log_message("User entered invalid address")
                    logger.end_session()

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