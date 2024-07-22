cmake_minimum_required(VERSION 3.10)
project(test_project)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include the subdirectory for headers and source files
include_directories(${PROJECT_SOURCE_DIR}/sub_dir)

# Add the executable target
add_executable(test_project main.cpp sub_dir/helper_1.cpp sub_dir/helper.cpp)
