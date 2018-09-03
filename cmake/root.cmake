cmake_minimum_required(VERSION 3.0)
project(qub3d)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

add_subdirectory(qub3d-libdeps)

if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/qub3d-engine)
    add_subdirectory(qub3d-engine)
endif()

if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/sandblox-client)
    add_subdirectory(sandblox-client)
endif()

if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/sandblox-launcher)
    add_subdirectory(sandblox-launcher)
endif()
