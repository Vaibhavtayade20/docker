from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to python flask app version1"


@app.route("/name", methods=["GET"])
def name():
    return "Vaibhav Tayade"

# run the application
app.run(host="0.0.0.0", port=9000, debug=True)

