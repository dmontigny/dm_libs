""" this class contains tools for working with json files. """

import os
import sys
from os import path
import json

# if "dm_libs" not in sys.path:
#     sys.path.append(os.path.abspath('..\\..\\dm_libs'))

# TODO: find reference to cls_logger
from cls_logger import ClassLog

jlogger = ClassLog()


class ClassJSON(object):
    def __init__(self, log=True):
        self.log = log
        if self.log:
            jlogger.get_logger('cls_logger')
        self.json = None
        self.tops = []
        if self.log:
            jlogger.logger.info("Class_JSON module loaded.")

    def read_json(self, jfile):
        with open(jfile, "r") as read_file:
            self.json = json.load(read_file)
            read_file.close()
        if self.log:
            jlogger.logger.info(f"{jfile} file read")
        return self.json

    def parse_json(self, show=True):
        def get_subs(loc, spc=""):
            if isinstance(loc, dict):
                for k, v in loc.items():
                    if k[0] == "\\":
                        if show:
                            print(f"{spc}   {k[1:]}")
                        get_subs(v, "   ")
                    elif v[0] == "\\":
                        if show:
                            print(f"{spc}   \\{v}")
                    else:
                        if show:
                            print(f"{spc}   {k}: {v}")
            elif isinstance(loc, list):
                for v in loc:
                    if show:
                        print(f"{spc}      {v}")

        for top, top_v in self.json.items():
            self.tops.append(top)
            if show:
                print("Top level:", top)
            for k, v in top_v.items():
                if k[0] == "\\":
                    if show:
                        print(f"{k[1:]}:")
                    get_subs(v)
                else:
                    if show:
                        print(f"{k}: {v}")

    def log_msg(self, msg):
        if self.log:
            jlogger.logger.info(msg)
