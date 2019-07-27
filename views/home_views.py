from flask import Blueprint, render_template

blueprint = Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
def home():
    return render_template("home/index.html")


@blueprint.route("/about")
def about():
    return render_template("home/about.html")