Introduce
=========
### Translation: [English](https://github.com/NaiveWang/captcha_recognize/blob/master/README.md) ~[中文](https://github.com/NaiveWang/captcha_recognize/blob/master/README-zhcn.md)~

CAPTCHA recognizing from with TensorFlow 1.14 GPU, preprocessing added(elimitate bars and stripes), run on Arch Linux with fresh cuda, python 3.7

This fork could recover from checkpoints, code has been modified to be compatible with python3 and latest tensorflow. Some utility tools has also been added to this fork to help with web spiders and raw dataset labeling.

Dependence
==========

### core `train` `recognize`

> system : linux ( prefer arch linux distros )

For an arch distro, there is no need to install specific version of cuda to match with tensorflow which is installed on pip, instead, installing both fresh cuda and tensorflow-opt-cuda from package manager **pacman** will suit deep learning rigs perfectly.

*Windows is deprecated due to directory conflicts.*

> python : python 3.x ( prefer python3.7)

> tensorflow/tensorflow-gpu 1.14.0 (gpu)

to test if your gpu rigs are working properly, please run this python3 [script](https://github.com/NaiveWang/Just_for_Fun/blob/master/Others/linux_gadgets/gpu_check_tensorflow.py) to check.

~### captcha~
~https://pypi.python.org/pypi/captcha/0.1.1~

**notice :**

**in this fork there is no need to generate captcha ourselves, we will claw and in some case automate them in purpose. While only methordology and local instance is provided for skirting privacy issues.**

### label marker `manual labelng` `permitive steps`

To boost label marking steps, a small flask web server is added to this fork, it grabs target captcha from local or target webset and show captcha on the web page, then type the captcha and submit, finally the labeled image will be stored locally.

> python flask

### preprocessor `image preprocessing` `noise elimiting`

some captcha has stripes and bars to mess up with automation, but in some case, some opencv and pixel algorithms could help with it.

> opencv-python

> pillow

### captcha crawler kit `automated labeling` `post steps`

>python flask

>selemium

### captcha recognize server

Usage
=====
## 1.prepare captchas
put your own captchas in **<current_dir>/data/train_data/** for training, **<current_dir>/data/valid_data/** for evaluating and **<current_dir>/data/test_data/** for recognize testing, images file name must be **label_\*.jpg** or **label_\*.png** and recommend size **128x48**. you can also use default generation:
```
python captcha_gen_default.py
```

## 2.convert dataset to tfrecords
the result file will be **<current_dir>/data/train.tfrecord** and **<current_dir>/data/valid.tfrecord**
```
python captcha_records.py
```

## 3.training
train and evaluate neural network on CPU or one single GPU
```
python captcha_train.py
```
you can also train over multiple GPUs
```
python captcha_multi_gpu_train.py
```

## 4.evaluate
```
python captcha_eval.py
```

## 5.recognize
read captchas from **<current_dir>/data/test_data/** for recogition
```
python captcha_recognize.py
```
result like this
```
...
image WFPMX_num552.png recognize ----> 'WFPMX'
image QUDKM_num468.png recognize ----> 'QUDKM'
```
