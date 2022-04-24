# UWE Assignment Year 3 | Digital Systems Project (DSP) | IdentiFlora: Houseplant Identification and Care Application

## The CNN
The CNN folder contains two subfolders, the first consisting of the prototype subdirectory which contains the Python code used for the initial prototype CNN implementation consisting of the CNNImagePreprocessor.py file that does the initial image pre-processing, PrototypeCNN.py that contains the code to generate the prototype CNN TensorFlow model and the Converter subdirectory, that contains the Python code that coverts a TensorFlow .h5 model into a .tflite model assigning metadata to the model in the process. In addition to this, this subfolder contains the premade datasets used for the initial training of the CNN and the initial TensorFlow and TensorFlow Lite implementation of the CNN. The CNN folder also contains the Full-Scale CNN subdirectory that contains the Python code used to create the final version of the CNN, the premade and handmade houseplant datasets used for the project, and the final version of the houseplant identification CNN TensorFlow Lite model.  

## The Database
The Database folder contains the Python code used to create the SQLite database, as well as the plantInformation.db SQLite database 

## The Mobile Application
The IdentiFlora folder contains the code for the final version of the artefact, the IdentiFlora Android Application, including the integrated CNN and the integrated database. To access this application and run it on your Android device it will need to be accessed and downloaded to your Android device in Android Studio.
