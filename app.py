from flask import Flask

app = Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from views import home_views

    app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
