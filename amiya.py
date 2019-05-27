import numpy as np
from keras.preprocessing.image import load_img
import tensorflow as tf
from keras.preprocessing import image


def perd(img_path):
    img = load_img(img_path)
    img = image.img_to_array(img)
    img = np.resize(img, (128,128,3))
    img = np.expand_dims(img, axis=0)
    img = img / 255.
    model = tf.keras.models.load_model('../homework/static/model/amiya.h5')
    return model.predict(img)

