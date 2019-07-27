from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
application = app

@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/about")
def about():
    return render_template("home/about.html")


if __name__ == '__main__':
    app.run(debug=False)
