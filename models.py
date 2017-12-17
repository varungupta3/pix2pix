import tensorflow as tf
from layers import *
import pdb

def photo_to_sketch_generator(x, batch_size, is_train, reuse):

  with tf.variable_scope('GEN', reuse=reuse) as vs:

    with tf.variable_scope('Encoder', reuse=reuse) as vs_enc:
      with tf.variable_scope('conv1', reuse=reuse):
        hidden_num = 64
        x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('conv2', reuse=reuse):
        hidden_num *= 2
        x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('conv3', reuse=reuse):
        hidden_num *= 2
        x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('conv4', reuse=reuse):
        hidden_num *= 2
        x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('conv5', reuse=reuse):
        hidden_num *= 2
        x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('conv6', reuse=reuse):
        x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
        print (x.shape)

      # with tf.variable_scope('deconv5', reuse=reuse):
      #   hidden_num /= 2
      #   x = t_conv_factory(x, hidden_num,[batch_size,32,32,4] ,3, 1, is_train, reuse)
      #   print (x.shape)

      with tf.variable_scope('dropout', reuse=reuse):
        x = tf.nn.dropout(x, keep_prob=0.5)
        print ('Dropout layer : ', x.shape)

    with tf.variable_scope('Decoder', reuse=reuse) as vs_dec:
      with tf.variable_scope('deconv1', reuse=reuse):
        out_channels = hidden_num
        x = t_conv_factory_leaky(x, hidden_num, [batch_size,7,8,out_channels], 3, 1, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('deconv2', reuse=reuse):
        hidden_num /= 2
        out_channels = hidden_num
        x = t_conv_factory_leaky(x, hidden_num, [batch_size,13,16,out_channels], 3, 1, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('deconv3', reuse=reuse):
        hidden_num /= 2
        out_channels = hidden_num
        x = t_conv_factory_leaky(x, hidden_num, [batch_size,25,32,out_channels], 3, 1, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('deconv4', reuse=reuse):
        hidden_num /= 2
        out_channels = hidden_num
        x = t_conv_factory_leaky(x, hidden_num, [batch_size,50,63,out_channels], 3, 1, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('deconv5', reuse=reuse):
        hidden_num /= 2
        out_channels = hidden_num
        x = t_conv_factory_leaky(x, hidden_num, [batch_size,100,125,out_channels], 3, 1, is_train, reuse)
        print (x.shape)

      with tf.variable_scope('deconv6', reuse=reuse):
        hidden_num = 1
        out_channels = hidden_num
        x = t_conv_factory_leaky(x, hidden_num, [batch_size,200,250,out_channels], 3, 1, is_train, reuse)
        print (x.shape)


    pdb.set_trace()

    variables = tf.contrib.framework.get_variables(vs)
    return x,variables


def discriminator(x, batch_size, is_train, reuse):
  
  with tf.variable_scope('DIS', reuse=reuse) as vs:
    with tf.variable_scope('conv1', reuse=reuse):
      hidden_num = 4
      x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
      # x = tf.nn.avg_pool(x, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
      print (x.shape)

    # conv2
    with tf.variable_scope('conv2', reuse=reuse):
      hidden_num *= 2
      x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
      # x = tf.nn.avg_pool(x, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
      print (x.shape)

    with tf.variable_scope('conv3', reuse=reuse):
      hidden_num *= 2
      x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
      # x = tf.nn.avg_pool(x, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
      print (x.shape)

    with tf.variable_scope('conv4', reuse=reuse):
      hidden_num *= 2
      x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
      # x = tf.nn.avg_pool(x, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
      print (x.shape)

    with tf.variable_scope('conv5', reuse=reuse):
      hidden_num *= 2
      x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
      # x = tf.nn.avg_pool(x, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
      print (x.shape)

    with tf.variable_scope('conv6', reuse=reuse):
      hidden_num *= 2
      x = conv_factory_leaky(x, hidden_num, 3, 2, is_train, reuse)
      # x = tf.nn.avg_pool(x, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
      print (x.shape)

    with tf.variable_scope('fc1', reuse=reuse):
      x = tf.reshape(x, shape = [batch_size, -1])
      x = fc_factory_leaky(x, 100, is_train, reuse)
      print (x.shape)

    with tf.variable_scope('fc_out', reuse=reuse):
      # x = tf.reshape(x, shape = [batch_size, -1])
      x = fc_factory_noact(x, 1, is_train, reuse)
      print (x.shape)
      # x = tf.nn.sigmoid(x)

  variables = tf.contrib.framework.get_variables(vs)
  return x, variables