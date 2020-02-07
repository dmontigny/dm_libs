

import logging
from os import path, walk

# from os import listdir
# from os.path import isfile, join


class ClassBrowser(object):
    def __init__(self):
        self.location = None
        self.folders = None
        self.files = None
        self.target = None
        logger = logging.getLogger('spam_application')

    def get_dirs(self, location="S:\OBC"):
        self.location = path.normpath(location)
        if self.location[0] == "\\" and self.location[1] != "\\":
            self.location = "\\" + self.location

        # TODO: cannot read network share folders
        self.logger.info(f'getting sub-dirs at {self.location}')
        self.folders = []
        for root, dirs, files in walk(self.location):
            for loc in dirs:
                self.folders.append(path.join(root, loc))
            for file in files:
                self.folders.append(path.join(root, file))
                pass

        self.logger.info(f'found {len(self.folders)} folders at {self.location}')

    def show_dirs(self):
        self.logger.info('showing sub-dirs at {}'.format(self.location))
        for folder in self.folders:
            self.logger.debug(folder)

    def search_4_text(self, target_ext, target_text):
        self.logger.info(f'searching for {str(target_text)}')
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
        self.logger.info(f'searching for {str(target_file).lower()}')
        self.target_file = str(target_file).lower()
        for folder in self.folders:
            if self.target_file in str(folder).lower():
                print(folder)


