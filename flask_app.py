from flask import Flask, render_template, request
from docs import application

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_name', methods=["POST"])
def get_name():
    name = request.form.get("name")
    print(name)
    app_res = application.main(name)
    if app_res == "no_name":
        return render_template("no_name.html")
    return render_template(name + "_map.html")


if __name__ == "__main__":
    app.run()
