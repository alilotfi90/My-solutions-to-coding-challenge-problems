import tensorflow as tf
from tensorflow.keras import layers


def get_image_preprocessing_pipeline(input_size, resize):
    image_prep_pipeline = tf.keras.Sequential([
        layers.Resizing(height=resize,width=resize),
        layers.Rescaling(1.0/255),
        layers.RandomFlip("horizontal_and_vertical"),
        layers.RandomRotation(0.1),
        layers.RandomContrast(0.1),
        layers.RandomCrop(int(resize*0.9),int(resize*0.9),3),
        layers.RandomZoom(height_factor=0.1,width_factor=0.1),
        layers.RandomTranslation(height_factor=0.1,width_factor=0.1),
        layers.RandomBrightness(factor=0.1),
        ])
    image_prep_pipeline.build(input_shape=(input_size,input_size,3))
    return image_prep_pipeline