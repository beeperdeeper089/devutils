import os
import shutil

class Wendy(object):
    def __init__(self, targetUser)
        self.targetUser = targetUser

    def generate():
        script_dir = str(os.path.dirname(os.path.realpath(__file__)))

        root_dir = script_dir + "/../" + self.targetUser + "/"
        cmake_dir = script_dir + "/resources/cmake/"

        shutil.copyfile(cmake_dir + "root.cmake", root_dir + "CMakeLists.txt")
