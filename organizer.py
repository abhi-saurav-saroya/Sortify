import os
import shutil
import time
import logger

import config

def organize(folder_path: str) -> tuple[bool, dict]:
    files = os.listdir(folder_path)
    
    full_paths = []
    for file in files:
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):       # ignoring subdirectories
            full_paths.append(full_path)

    success = True
    moved_files_info = {
        "Renamed" : 0
    }

    total = len(full_paths)
    for index, full_path in enumerate(full_paths, start=1):
        category = get_category(full_path)
        destination_folder = create_category_folder(folder_path, category)
        if destination_folder is None:
            success = False
            logger.log_message(
                f"Failed to create folder for category {category}"
            )
            continue

        filename = os.path.basename(full_path)
        print(f"[{index}/{total}] Processing {filename}")
        time.sleep(0.1)

        destination_path, rename_occurred = get_unique_destination_path(destination_folder, full_path)
        
        if move_file(full_path, destination_path):
            add_into_moved_files_statistic(moved_files_info, category, rename_occurred)
            logger.log_message(
                f"Moved {filename} -> {destination_path}"
            )
        else:
            success = False
            logger.log_message(
                f"Failed to move {filename}"
            )
            continue
        
    return success, moved_files_info
    


def get_category(full_path: str) -> str:
    _, extension = os.path.splitext(full_path)

    category = config.FILE_TYPES.get(
        extension.lower(),
        config.DEFAULT_CATEGORY
    )

    return category



def create_category_folder(folder_path: str, category: str) -> str | None:
    try: 
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(
            destination_folder,
            exist_ok=True
        )
    except OSError:
        destination_folder = None

    return destination_folder



def move_file(full_path: str, destination_path: str) -> bool:
    try:
        shutil.move(full_path, destination_path)
        return True
    except OSError:
        return False
    


def add_into_moved_files_statistic(moved_files_info: dict, category: str, rename_occurred: bool):
    moved_files_info[category] = (
        moved_files_info.get(category, 0) + 1
    )

    if rename_occurred:
        moved_files_info["Renamed"] = (
            moved_files_info.get("Renamed", 0) + 1
        )



def get_unique_destination_path(destination_folder: str, full_path: str) -> tuple[str, bool]:

    rename_occurred = False

    filename = os.path.basename(full_path)

    destination_path = os.path.join(
        destination_folder,
        filename
    )

    if not os.path.exists(destination_path):
        return destination_path, rename_occurred

    name, extension = os.path.splitext(filename)

    counter = 1

    while True:
        rename_occurred = True

        new_filename = (
            f"{name}({counter}){extension}"
        )

        destination_path = os.path.join(
            destination_folder,
            new_filename
        )

        if not os.path.exists(destination_path):
            logger.log_message(
                f"Renamed {filename} -> {new_filename}"
            )
            return destination_path, rename_occurred

        counter += 1