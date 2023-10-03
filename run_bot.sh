#!/bin/bash

# Change directory to tflite1
cd tflite1

# Activate the virtual environment
source tflite1-env/bin/activate

# Run the Python script with the specified arguments
python3 object_voice_webcam.py --modeldir=Sample_TFLite_model
