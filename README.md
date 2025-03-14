# Face Detection with OpenCV

This project detects faces in an image using OpenCV's Haar cascade classifier. The input image is resized while maintaining its aspect ratio, and detected faces are highlighted with red rectangles.

## Features
- Reads an image and resizes it to fit within 800x600 pixels.
- Converts the image to grayscale for better face detection.
- Detects faces using OpenCV’s pre-trained Haar cascade model.
- Draws a red rectangle around each detected face.
- Displays the processed image with detected faces.
- Saves the output image only if faces are detected.

## Requirements
Make sure you have Python installed along with the required dependencies:

```bash
pip install opencv-python
