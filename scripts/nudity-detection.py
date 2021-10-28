from nudenet import NudeClassifier
from nudenet import NudeDetector
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Method to classify a given image as safe or unsafe
def classify(img):
    classifier = NudeClassifier()
    return classifier.classify(img)


# Detector to detect all exposed body parts in the image
def detect(img):
    detector = NudeDetector()
    return detector.detect(img)


# Method to display the images
def displayImage(img):
    image = mpimg.imread(img)
    plt.imshow(image)
    plt.show()


def main():
    path = "C:/Users/yash4/OneDrive/Desktop/images/"
    for images_to_classify in os.listdir(path):
        classifierResult = classify(path + images_to_classify)
        detectorResult = detect(path + images_to_classify)
        # displayImage(path + images_to_classify)
        print(images_to_classify + ":")
        print(
            str(classifierResult[path + images_to_classify]["safe"])
            + " "
            + str(classifierResult[path + images_to_classify]["unsafe"])
        )
        for dictionary in detectorResult:
            print(dictionary["label"], end=" ")
        print("\n")


main()
