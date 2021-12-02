import argparse
import warnings
import numpy as np
import os
import pickle
import sys
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Comme mon modèle est basé sur EfficientNet, j'utilise cette méthode
from tensorflow.keras.applications.efficientnet import preprocess_input

# Le modèle entrainé via les notebooks.
MODEL = "efficientnet_120_augmented.h5"

# Les classes (les 120 races de chiens)
CLASSES = "class_names.pkl"


def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Run inference on an input image")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input image file"

    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')

    # -- Create the arguments
    required.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def infer_on_image(args):
    '''
    Performs inference on image - main method
    '''
    # Test and parse the "-i" argument
    if args.i is None or len(args.i) == 0:
        sys.exit('Error : please provide an image file (ex: python eval.py -i image.jpg)')

    if not os.path.isfile(args.i):
        sys.exit('Error : file "{0}" not found'.format(args.i))

    img = image.load_img(args.i, target_size=(224, 224))
    model = tf.keras.models.load_model(MODEL)
    class_names = pickle.load(open(CLASSES, 'rb'))

    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)  # batch d'une seule image
    img_preprocessed = preprocess_input(img_batch)  # normalisation

    prediction = model.predict(img_preprocessed)

    top_indices = prediction[0].argsort()[-3:][::-1]
    predicted_races = [class_names[i] for i in top_indices]
    predicted_races.sort(key=lambda x: x[2], reverse=True)

    print("============== RESULT ==============")
    i = 0
    for predicted in predicted_races:
        prob = prediction[0][top_indices[i]]
        i = i + 1
        print(str(i), predicted.split('-')[1], '(' + str(round(prob * 100)) + '%)')
    print("====================================")


def main():
    args = get_args()
    infer_on_image(args)


warnings.filterwarnings("ignore")
if __name__ == "__main__":
    main()
