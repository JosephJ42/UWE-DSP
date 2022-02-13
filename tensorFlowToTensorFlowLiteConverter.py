#Convert a standard tensorflow model into a a TensorFlow Lite model
import tensorflow as tf

tfModelLocation = "D:/UWE-DSP/CNN/Prototype/identiFloraCNNModel.h5"


# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(tfModelLocation) # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)