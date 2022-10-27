from os.path import *
import sys


def fix_path(relative_path):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return normpath(join(getattr(sys, "_MEIPASS"), relative_path))
    else:
        return normpath(relative_path)
