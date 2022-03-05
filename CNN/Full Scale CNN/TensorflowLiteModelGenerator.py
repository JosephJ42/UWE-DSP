
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
train_data, rest_data = data.split(0.8)
validation_data, test_data = rest_data.split(0.5)

model = image_classifier.create(train_data, validation_data=validation_data, epochs=15)

loss, accuracy = model.evaluate(test_data)

model.summary()

model.export(export_dir='.')

model.export(export_dir='.', export_format=ExportFormat.LABEL)

model.evaluate_tflite('model.tflite', test_data)
