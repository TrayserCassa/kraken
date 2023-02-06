#!/usr/bin/python

import yaml
from flask import Flask, render_template


app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    with open("services.yaml", "r") as f:
        targets = yaml.safe_load(f)

    return render_template("main.html.j2", targets=targets)


if __name__ == "__main__":
    app.run(debug=True)
