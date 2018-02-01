from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import os
import base64
from io import BytesIO
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

FLAGS = None

def vec_to_png(data, rows, cols):
  image_array = 255 - np.reshape(data,(28,28))*255
  pil_img = Image.fromarray(image_array).convert('L')
  buffer = BytesIO()
  pil_img.save(buffer, format="PNG")
  return base64.b64encode(buffer.getvalue()).decode("utf-8")

def main(_):
  data_dir = '/tmp/tensorflow/mnist/input_data'
  mnist = input_data.read_data_sets(data_dir, one_hot=True)
  x = tf.placeholder(tf.float32, [None, 784])
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  y = tf.matmul(x, W) + b
  y_ = tf.placeholder(tf.float32, [None, 10])

  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()

  for e, _ in enumerate(range(1000)):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  # Test trained model
  for e, _ in enumerate(range(5)):
    guess_y = sess.run(tf.argmax(y, 1), feed_dict={x: [mnist.test.images[e]]})[0]
    print('Guess:', guess_y, '| Value:', list(mnist.test.labels[e]).index(1))
    print(vec_to_png(mnist.test.images[e], 28, 28))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)