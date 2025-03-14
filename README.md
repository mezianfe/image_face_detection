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

`pip install opencv-python`

## How to Use
1. Upload an image named **"your_image.jpg"** to the project folder.
2. Run the script:

`python face.py your_image.jpg`

3. The detected faces will be displayed, and if any faces are found, the modified image will be saved as `your_image_with_faces.jpg`.

## Notes
- You can use any image, but it must be named **"your_image.jpg"** before running the script.
- Adjust `scaleFactor` and `minNeighbors` in the script for better detection accuracy.
- If no faces are detected, the output image will not be saved.


## License
This project is open-source and free to use.
