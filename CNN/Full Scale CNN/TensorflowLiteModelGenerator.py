import os

import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader

training_data_path = "D:/UWE-DSP/CNN/Full Scale CNN/training"

data = DataLoader.from_folder(training_data_path)
train_data, test_data = data.split(0.9)

model = image_classifier.create(train_data, epochs=10)

loss, accuracy = model.evaluate(test_data)

model.summary()

model.export(export_dir='.')

model.export(export_dir='.', export_format=ExportFormat.LABEL)

model.evaluate_tflite('model.tflite', test_data)