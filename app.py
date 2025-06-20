
from flask import Flask, request, jsonify, render_template
from zodiac_utils import pipei

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/match", methods=["POST"])
def pipei_api():
    shuju = request.get_json()
    shengri = shuju.get("birthday")
    xingbie = shuju.get("gender")
    jieguo = pipei(shengri, xingbie)
    return jsonify(jieguo)

@app.route("/match_form", methods=["POST"])
def pipei_form():
    shengri = request.form.get("birthday")
    xingbie = request.form.get("gender")
    jieguo = pipei(shengri, xingbie)
    return render_template("index.html", result=jieguo)

if __name__ == "__main__":
    app.run(debug=True)
