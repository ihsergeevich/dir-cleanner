import os

from scanner import Scanner


class Cleaner(Scanner):

    def __init__(self, start_path, flag):
        super().__init__(start_path)
        self.flag = flag

    def remove(self) -> None:
        doc_files = []
        bak_files = []

        files_path, empty_dirs = self.sort_dirs()

        for path, files_name in files_path.items():
            for file_name in files_name:
                if file_name.endswith('.bak'):
                    bak_files.append(path + file_name[:-4])

                elif file_name.endswith('.doc'):
                    doc_files.append(path + file_name[:-4])

        for path in (set(doc_files) ^ set(bak_files)):
            if path in bak_files:
                os.remove(path + '.bak')

        if self.flag:
            for dir_ in empty_dirs:
                os.rmdir(dir_)
