#Convert a standard tensorflow model into a a TensorFlow Lite model
import tensorflow as tf

tfModelLocation = "D:/UWE-DSP/CNN/Prototype/Converter/identiFloraCNNModel.h5"
savedTFLiteModelLocation = "D:/UWE-DSP/CNN/Prototype/Converter/identiFloraCNNModel.tflite"


# Convert the model
model = tf.keras.models.load_model(tfModelLocation)

converter = tf.lite.TFLiteConverter.from_keras_model(model) # path to the SavedModel directory

tflite_model = converter.convert()

# Save the model.
with open(savedTFLiteModelLocation, 'wb') as f:
  f.write(tflite_model)