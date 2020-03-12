
from os import path, walk
import os
import sys
from platform import system

if "dm_libs" not in sys.path:
    sys.path.append(os.path.abspath('..\\..\\dm_libs'))
else:
    print("PRESENT!")

# import cls_logger
from cls_logger import ClassLog

# print(f"os.path = {os.path}")
# print("sys.path:")
# for item in sys.path:
#     print(item)

mylogger = ClassLog
op_sys = ('Windows', 'Linux')[system() == 'Windows']
# mylogger = cls_logger.ClassLog()


class ClassBrowser(object):
    def __init__(self, log=True):
        self.log = log
        if self.log:
            mylogger.get_Logger('cls_files')
        self.location = None
        self.tree = {}
        self.folders = {}
        self.files = {}
        self.target = None
        if self.log:
            mylogger.info(f'file searcher created')

    def get_tree(self, location="S:\OBC"):
        self.location = path.normpath(location)
        print(f"get tree: {self.location}")
        if self.location[0] == "\\" and self.location[1] != "\\":
            self.location = "\\" + self.location

        # TODO: cannot read network share folders
        if self.log:
            mylogger.info(f'getting files at {self.location}')
        self.files = {}
        for root, dirs, files in walk(self.location):
            for loc in dirs:
                self.tree[loc] = path.join(root, loc)
            for file in files:
                self.tree[file] = path.join(root, file)
                # self.tree[file.split(("\\", "/")[op_sys == "Windows"])[-1]] = path.join(root, file)

        if self.log:
            mylogger.info(f'found {len(self.files)} folders at {self.location}')
        return self.tree

    def get_dirs(self, location="S:\OBC"):
        self.location = path.normpath(location)
        print(f"get dirs: {self.location}")
        if self.location[0] == "\\" and self.location[1] != "\\":
            self.location = "\\" + self.location

        # TODO: cannot read network share folders
        if self.log:
            mylogger.info(f'getting sub-dirs at {self.location}')
        # self.folders = []
        for root, dirs, files in walk(self.location):
            for loc in dirs:
                self.folders[loc] = path.join(root, loc)

        if self.log:
            mylogger.info(f'found {len(self.folders)} folders at {self.location}')
        return self.folders

    def get_files(self, location="S:\OBC"):
        self.location = path.normpath(location)
        print(f"get files: {self.location}")
        if self.location[0] == "\\" and self.location[1] != "\\":
            self.location = "\\" + self.location

        # TODO: cannot read network share folders
        if self.log:
            mylogger.info(f'getting files at {self.location}')
        self.files = {}
        for root, dirs, files in walk(self.location):
            for file in files:
                self.files[file.split(("\\", "/")[op_sys == "Windows"])[-1]] = self.location

        # print(f"self.files: {self.files}")
        if self.log:
            mylogger.info(f'found {len(self.files)} folders at {self.location}')
        return self.files



    def search_4_text(self, target_ext, target_text):
        if self.log:
            mylogger.info(f'searching for {str(target_text)}')
        self.target_ext = str(target_ext)
        self.target_text = str(target_text)
        for folder in self.folders:
            for file in self.files:
                print(folder)
                if self.target_ext in str(file).lower():
                    f = open(self.target_text, "r")
                    for line in f:
                        print(line)

    def search_4_files(self, target_file):
        if self.log:
            mylogger.info(f'searching for {str(target_file).lower()}')
        self.target_file = str(target_file).lower()
        for folder in self.folders:
            if self.target_file in str(folder).lower():
                print(folder)

    # def show_dirs(self):
    #     if self.log:
    #         mylogger.info('showing sub-dirs at {}'.format(self.location))
    #     for folder in self.folders:
    #         mylogger.debug(folder)

