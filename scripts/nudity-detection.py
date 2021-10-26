from nudenet import NudeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


def classify(path):
    classifier = NudeClassifier()
    for images_to_classify in os.listdir(path):
        # image = mpimg.imread(path + images_to_classify)
        result = classifier.classify(path + images_to_classify)
        print(images_to_classify)
        print("Unsafe " + str(result[path + images_to_classify]["unsafe"]))
        print("Safe " + str(result[path + images_to_classify]["safe"]))
        # plt.imshow(image)
        # plt.show()


def main():
    path = "C:/Users/yash4/OneDrive/Desktop/images/"
    classify(path)


main()
