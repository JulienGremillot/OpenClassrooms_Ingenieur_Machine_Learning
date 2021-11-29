import gradio as gr
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

# Le modèle entrainé via les notebooks.
MODEL = "efficientnet_120_augmented.h5"

# Les classes (les 120 races de chiens)
CLASSES = "class_names.pkl"


def infer_on_image(input_img):
    """
    Performs inference on image - main method
    """

    img_array = image.img_to_array(input_img)
    img_batch = np.expand_dims(img_array, axis=0)  # batch d'une seule image
    img_preprocessed = preprocess_input(img_batch)  # normalisation

    prediction = model.predict(img_preprocessed)

    top_indices = prediction[0].argsort()[-3:][::-1]
    predicted_races = [class_names[i] for i in top_indices]
    predicted_races.sort(key=lambda x: x[2], reverse=True)

    res = "============== RESULT ==============\n"
    i = 0
    for predicted in predicted_races:
        prob = prediction[0][top_indices[i]]
        i = i + 1
        res = res + str(i) + " " + predicted.split('-')[1] + " (" + str(round(prob * 100)) + "%)\n"
    res = res + "====================================\n"

    return res


model = tf.keras.models.load_model(MODEL)
class_names = pickle.load(open(CLASSES, 'rb'))

iface = gr.Interface(infer_on_image, gr.inputs.Image(shape=(224, 224)), "text")

iface.launch()
