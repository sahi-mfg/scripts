import os
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def empty_trash() -> None:
    """
    Empty the trash folder in the system.

    Args:
        None

    Returns:
        None

    """
    trash_folder = os.path.expanduser("~/.Trash")
    logging.info(f"Emptying trash folder: {trash_folder}")
    for filename in os.listdir(trash_folder):
        file_path = os.path.join(trash_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            logging.info(f"Removed {filename}")
    logging.info("Trash folder is empty now.")


if __name__ == "__main__":
    empty_trash()
