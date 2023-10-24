
# Api call using Flask #
# Jsonify is java script object notation #

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "The white man is in the forest"


if __name__=="__main__":
    app.run(debug=True)