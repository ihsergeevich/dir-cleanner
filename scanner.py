import os
from typing import Tuple


class Scanner:

    def __init__(self, start_path):
        self.start_path = start_path

    def sort_dirs(self) -> Tuple[dict, list]:
        files_list = {}
        empty_dirs = []

        for dirpath, dirnames, files in os.walk(self.start_path):
            files_list[dirpath] = []

            if files:
                for file in files:
                    files_list[dirpath].append(file)

            elif not files:
                empty_dirs.append(dirpath)

        return files_list, empty_dirs
