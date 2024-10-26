import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_folder(folder: str) -> None:
    """
    Organize the files in the folder based on their filetypes.
    
    Args:
        folder : str : The folder path to organize

    Returns:
        None
    
    """
    filetypes: dict[str, list[str]] = {
        'Images': ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.bpg', '.svg', '.heif', '.psd'],
        'Videos': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],
        'Documents': ['.oxps', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods', '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt'],
        'Archives': ['.a', '.ar', '.cpio', '.iso', '.tar', '.gz', '.rz', '.7z', '.dmg', '.rar', '.xar', '.zip'],
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file_path)[1].lower()
            for folder_name, extensions in filetypes.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    logging.info(f"Moved {filename} to {folder_name}")


if __name__ == '__main__': 
    folder: str = '/Users/sahi/Downloads'
    organize_folder(folder)