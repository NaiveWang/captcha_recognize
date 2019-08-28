from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
from datetime import datetime
import argparse
import sys

import tensorflow as tf

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import captcha_model as captcha



FLAGS = None

def run_train():
  """Train CAPTCHA for a number of steps."""

  with tf.Graph().as_default():
    images, labels = captcha.inputs(train=True, batch_size=192)

    logits = captcha.inference(images, keep_prob=0.6)

    loss = captcha.loss(logits, labels)

    train_op = captcha.training(loss)

    saver = tf.compat.v1.train.Saver()

    init_op = tf.group(tf.global_variables_initializer(),
                       tf.local_variables_initializer())

    sess = tf.compat.v1.Session()

    #sess.run(init_op)
    try:
        #saver.restore(sess, FLAGS.checkpoint)
        saver.restore(sess, tf.train.latest_checkpoint(FLAGS.checkpoint_dir))
    except Exception as e:
        print(e)
        sess.run(init_op)
        #exit()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    try:
      _loss=100000
      step = 0
      while not coord.should_stop():
        start_time = time.time()
        _, loss_value = sess.run([train_op, loss])
        duration = time.time() - start_time
        if step % 10 == 0:
          print('>> Step %d run_train: loss = %f (%.4f sec)' % (step, loss_value,
                                                     duration))
        if _loss > loss_value:
          print('>> %s STEP %d LOSS %f SPAN %.4f' % (datetime.now(), step, loss_value, duration))
          saver.save(sess, FLAGS.checkpoint, global_step=step)
          _loss = loss_value
        #open('learning.log', 'a').write(step.__str__()+'\t'+loss_value.__str__()+'\n')
        step += 1
    except Exception as e:
      #print('>> %s STEP:' % (datetime.now()))
      saver.save(sess, FLAGS.checkpoint, global_step=step)
      coord.request_stop(e)
    finally:
      coord.request_stop()
    coord.join(threads)
    sess.close()


def main(_):
  #open("learning.log","w").write('')
  #if tf.gfile.Exists(FLAGS.train_dir):
  #  tf.gfile.DeleteRecursively(FLAGS.train_dir)
  #tf.gfile.MakeDirs(FLAGS.train_dir)
  run_train()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--batch_size',
      type=int,
      default=128,
      help='Batch size.'
  )
  parser.add_argument(
      '--train_dir',
      type=str,
      default='./captcha_train',
      help='Directory where to write event logs.'
  )
  parser.add_argument(
      '--checkpoint_dir',
      type=str,
      default='./captcha_train',
      help='Directory where to restore checkpoint.'
  )
  parser.add_argument(
      '--checkpoint',
      type=str,
      default='./captcha_train/captcha',
      help='Directory where to write checkpoint.'
  )
  FLAGS, unparsed = parser.parse_known_args()
  tf.compat.v1.app.run(main=main, argv=[sys.argv[0]] + unparsed)
