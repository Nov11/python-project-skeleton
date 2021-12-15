set(SOURCE
        kernel/zero_out_kernel.cpp
        op/zero_out_op.cpp)

add_library(tf_op SHARED ${SOURCE})



find_library(TF_FRAMEWORK_LIBRARY libtensorflow_framework.so.2 HINTS ${TF_LIB})
message(STATUS "TF_FRAMEWORK_LIBRARY : ${TF_FRAMEWORK_LIBRARY}")
target_link_libraries(tf_op ${TF_FRAMEWORK_LIBRARY})

set_target_properties(tf_op PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/out/library)