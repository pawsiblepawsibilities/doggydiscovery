import cv2
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from keras.applications.resnet_v2 import preprocess_input
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'labels.csv')
df_labels = pd.read_csv(csv_file_path)
num_breeds = 120
im_size = 224
batch_size = 64
encoder = LabelEncoder()
breed_dict = list(df_labels['breed'].value_counts().keys())
new_list = sorted(breed_dict, reverse=True)[:num_breeds * 2 + 1:2]
df_labels = df_labels.query('breed in @new_list')
model = load_model("data/model")


def top_predictions(pred_img_path):
    pred_img_array = cv2.resize(cv2.imread(pred_img_path, cv2.IMREAD_COLOR), (im_size, im_size))
    pred_img_array = preprocess_input(
        np.expand_dims(np.array(pred_img_array[..., ::-1].astype(np.float32)).copy(), axis=0))
    pred_val = model.predict(np.array(pred_img_array, dtype="float32"))
    return sorted(new_list)[np.argmax(pred_val)]
