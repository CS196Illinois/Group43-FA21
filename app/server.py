from flask import Flask, redirect, url_for, request
from os import system
from os import listdir
from scripts.nudity_detection import classify
from scripts.nudity_detection import detect
from scripts.nudity_detection import display_image
from scripts.image_downloader import image_download

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    request_data = request.get_json()
    url = request_data["url"]
    load_images(url)
    nudity_detect()


def nudity_detect():
    path = r"C:\Users\yash4\coding_projects\Group43_FA21\images"
    for images_to_classify in listdir(path):
        classifier_result = classify(path + images_to_classify)
        detector_result = detect(path + images_to_classify)
        print(images_to_classify + ":")
        print(
            str(classifier_result[path + images_to_classify]["safe"])
            + " "
            + str(classifier_result[path + images_to_classify]["unsafe"])
        )
        for dictionary in detector_result:
            print(dictionary["label"], end=" ")
        print("\n")


# call method to load all images in images folder
def load_images(url):
    image_download(url, "images")


if __name__ == "__main__":
    app.run(debug=True)
