import shutil, os

print ( "------------------ GENERATING CMAKE ------------------" )

script_dir = str( os.path.dirname( os.path.realpath( __file__ ) ) )

root_dir = script_dir + "/../"
cmake_dir = script_dir + "/resources/cmake/"

shutil.copyfile ( cmake_dir + "root.cmake", root_dir + "CMakeLists.txt" )
