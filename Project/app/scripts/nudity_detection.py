from nudenet import NudeClassifier
from nudenet import NudeDetector
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Method to classify a given image as safe or unsafe
def classify(img_path):
    classifier = NudeClassifier()
    return classifier.classify(img_path)


# Detector to detect all exposed body parts in the image
def detect(img_path):
    detector = NudeDetector()
    return detector.detect(img_path)


# Method to display the images
def display_image(img_path):
    image = mpimg.imread(img_path)
    plt.imshow(image)
    plt.show()
