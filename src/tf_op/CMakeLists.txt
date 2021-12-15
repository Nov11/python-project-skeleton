cmake_minimum_required(VERSION 3.17)
project(tf_op VERSION 1.0.0 DESCRIPTION "custom tensorflow op")

set(CMAKE_CXX_STANDARD 14)
set(CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g -gdwarf-4 -fno-omit-frame-pointer")

set(VENV_PATH ${PROJECT_SOURCE_DIR}/../../venv/lib/python3.8/site-packages)
set(TF_LIB ${VENV_PATH}/tensorflow/)
message(STATUS "TF_LIB: ${TF_LIB}")

set(TF_INC ${VENV_PATH}/tensorflow/include/)
message(STATUS "TF_INC: ${TF_INC}")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_GLIBCXX_USE_CXX11_ABI=0")

include_directories(${TF_INC})

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Flags: ${CMAKE_CXX_FLAGS}")


add_subdirectory(src)
add_subdirectory(test)