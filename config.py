# about captcha image
IMAGE_HEIGHT = 40
IMAGE_WIDTH = 100
CHAR_SETS = '2345678aAbBcdeEfFGHhKkMmNnPpQqRSsuvWwxYyz'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 5
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'
