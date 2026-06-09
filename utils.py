def is_path_valid(folder_path: str) -> bool:
    import os
    return os.path.isdir(folder_path)

def display_supported_extensions() -> None:
    import config

    supported_extensions = config.FILE_TYPES
    print("\nSupported Extensions:")

    for extension, folder in supported_extensions.items():
        print(f"\t{extension:<10} -> {folder}")