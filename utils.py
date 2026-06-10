def is_path_valid(folder_path: str) -> bool:
    import os
    return os.path.isdir(folder_path)



def display_supported_extensions() -> None:
    import config

    supported_extensions = config.FILE_TYPES
    print("\nSupported Extensions:")

    for extension, folder in supported_extensions.items():
        print(f"\t{extension:<10} -> {folder}")



def display_organization_statistics(moved_files_info: dict) -> str:
    print("Organization Statistics:")

    total_moved = 0
    for category, count in moved_files_info.items():
        total_moved += count
        print(f"\t{category:<15} -> {count}")

    print(f"Total Files Moved: {total_moved}")