from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def capture_url():
    request_data = request.get_json()
    url = request_data["url"]
    return """<h1>The url value is: {}</h1>""".format(url)


if __name__ == "__main__":
    app.run(debug=True)
