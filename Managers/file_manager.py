import os
import easygui

from Managers import excel_manager

my_path: str = os.getenv('APPDATA') + "\\Brosssh\\Rates"
file_path_file: str = "file_path"
complete_path = os.path.join(my_path, file_path_file)


def _user_choose_path() -> str:
    return easygui.fileopenbox(msg="Choose the destination Excel file.")


def _get_path_from_appdata() -> str | None:
    try:
        with open(complete_path, 'r') as r:
            data = r.read()
            return str(data)
    except (FileExistsError, FileNotFoundError) as e:
        os.makedirs(my_path, exist_ok=True)
        open(complete_path, 'x')
        return None


def get_valid_path() -> str:
    path_to_check = _get_path_from_appdata()
    is_validated_path: bool = False
    while not is_validated_path:
        try:
            # Check if excel_path is a valid file
            if not path_to_check or not os.path.exists(path_to_check):
                raise FileNotFoundError

            if not excel_manager.is_valid_excel_file(path_to_check):
                raise FileNotFoundError

            # File do exist
            with open(complete_path, 'w') as f:
                f.write(path_to_check)
            is_validated_path = True
            return path_to_check
        except FileNotFoundError as e:
            print(f"Please choose a valid file.")
            path_to_check = _user_choose_path()