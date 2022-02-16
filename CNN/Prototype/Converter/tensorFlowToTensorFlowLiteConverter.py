#Convert a standard tensorflow model into a a TensorFlow Lite model
import tensorflow as tf
import os

tfModelLocation = "D:/UWE-DSP/CNN/Prototype/Converter/identiFloraCNNModel.h5"
savedTFLiteModelLocation = "D:/UWE-DSP/CNN/Prototype/Converter/identiFloraCNNModel.tflite"


# Convert the model
model = tf.keras.models.load_model(tfModelLocation)

converter = tf.lite.TFLiteConverter.from_keras_model(model) # path to the SavedModel directory

tflite_model = converter.convert()

# Save the model.
with open(savedTFLiteModelLocation, 'wb') as f:
  f.write(tflite_model)


# add meta data

from tflite_support import flatbuffers
from tflite_support import metadata as _metadata
from tflite_support import metadata_schema_py_generated as _metadata_fb

# Creates model info.
model_meta = _metadata_fb.ModelMetadataT()
model_meta.name = "IdentiFlora's prototype CNN"
model_meta.description = ("Identify different species of house plant, this prototype model is a proof of concepts and only identifies 2 ")
model_meta.version = "v1"
model_meta.author = "Joseph Jarvis"
model_meta.license = ("Apache License. Version 2.0 http://www.apache.org/licenses/LICENSE-2.0.")

# creates input and output meta data
input_meta = _metadata_fb.TensorMetadataT()
output_meta = _metadata_fb.TensorMetadataT()

input_meta.name = "image"
input_meta.description = (  "Input image to be classified. The expected image is {0} x {1}, with three channels (red, blue, and green) per pixel."
                          "Each value in the tensor is a single byte between 0 and 180.".format(160, 160))

input_meta.content = _metadata_fb.ContentT()
input_meta.content.contentProperties = _metadata_fb.ImagePropertiesT()
input_meta.content.contentProperties.colorSpace = (
    _metadata_fb.ColorSpaceType.RGB)
input_meta.content.contentPropertiesType = (
    _metadata_fb.ContentProperties.ImageProperties)
input_normalization = _metadata_fb.ProcessUnitT()
input_normalization.optionsType = (
    _metadata_fb.ProcessUnitOptions.NormalizationOptions)
input_normalization.options = _metadata_fb.NormalizationOptionsT()
input_normalization.options.mean = [127.5]
input_normalization.options.std = [127.5]
input_meta.processUnits = [input_normalization]
input_stats = _metadata_fb.StatsT()
input_stats.max = [180]
input_stats.min = [0]
input_meta.stats = input_stats


# Creates output info.
output_meta = _metadata_fb.TensorMetadataT()
output_meta.name = "probability"
output_meta.description = "Probabilities of the 2 labels respectively."
output_meta.content = _metadata_fb.ContentT()
output_meta.content.content_properties = _metadata_fb.FeaturePropertiesT()
output_meta.content.contentPropertiesType = (
    _metadata_fb.ContentProperties.FeatureProperties)
output_stats = _metadata_fb.StatsT()
output_stats.max = [1.0]
output_stats.min = [0.0]
output_meta.stats = output_stats
label_file = _metadata_fb.AssociatedFileT()
label_file.name = os.path.basename("D:/UWE-DSP/CNN/Prototype/labels.txt")
label_file.description = "Labels for objects that the model can recognize."
label_file.type = _metadata_fb.AssociatedFileType.TENSOR_AXIS_LABELS
output_meta.associatedFiles = [label_file]


# Creates subgraph info.
subgraph = _metadata_fb.SubGraphMetadataT()
subgraph.inputTensorMetadata = [input_meta]
subgraph.outputTensorMetadata = [output_meta]
model_meta.subgraphMetadata = [subgraph]

b = flatbuffers.Builder(0)
b.Finish(
    model_meta.Pack(b),
    _metadata.MetadataPopulator.METADATA_FILE_IDENTIFIER)
metadata_buf = b.Output()

populator = _metadata.MetadataPopulator.with_model_file("D:/UWE-DSP/CNN/Prototype/Converter/identiFloraCNNModel.tflite")
populator.load_metadata_buffer(metadata_buf)
populator.load_associated_files(["D:/UWE-DSP/CNN/Prototype/labels.txt"])
populator.populate()
