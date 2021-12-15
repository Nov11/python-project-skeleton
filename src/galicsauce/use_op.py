import tensorflow._api.v2.compat.v1 as tf
import project_util

zero_out_module = tf.load_op_library(project_util.PROJECT_ROOT_DIR + '/src/tf_op/out/library/libtf_op.so')

if __name__ == '__main__':
    with tf.Session():
        ret = zero_out_module.zero_out([[1, 2], [3, 4]]).eval()
        print(ret)
