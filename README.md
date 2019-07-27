# TAMUSA-ACM Website
*This program is done with the Flask Micro-framework*


## Structure

**NOTE:** The hosting service we are using is cPanel, and it uses WSGI in the back-end that points directly to the application. The problem with this is that it causes issues with blueprints, which is the most ideal way to separate routes in Flask. Given that this isn't an option, all the routes must be in the app.py file. Just know that this isn't by design.


### Layout Template
- Start by creating a templates folder in the base project directory called `templates`
  - *Note:* Flask recongizes `templates` directory to be the base templates directory for HTML files automatically
- Next, create generic layout HTML file
  - Under the `templates` directory, create another directory called `shared`
  - From the `shared` folder, create an HTML file called `_layout.html`, this will be our "blueprint" HTML file that will be used for our jinja templating engine
  - *Note:* In this instance, we are using **bootstrap** for JS/CSS

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
    <title>{% block title %}Name of Page{% endblock %}</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
	      crossorigin="anonymous">

</head>
<body>
	{% block main_content %}{% endblock %}

<footer>
	<div class="copyright">
		Copyright &copy; Generic Company
	</div>
</footer>

</body>

</html>
```

- This will be used for your other HTML files, so now we will create a home/index page
  - Create `home` directory under the `templates` directory
  - Under `home` directory, create `index.html`; we will use jinja templating here to simply the pages and make changes where necessary

### Jinja Templating Modeling using Layout

```jinja
{% extends "shared/_layout.html" %}

{% block title %}
Generic Title
{% endblock %}

{% block main_content %}
<h1>Home Page</h1>
{% endblock %}
```

- Lastly, we will create `about.html` under `home` directory

```jinja
{% extends "shared/_layout.html" %}

{% block title %}
About Generic Company
{% endblock %}

{% block main_content %}
<h1>About</h1>
{% endblock %}
```

- Now that your templates are setup, we can start with the creation of the flask app


## Create Flask App
*Start by creating app.py*

### Blueprints and Routing

- Create blueprints that flask app can then register to view
- To understand this, we have to use "routing"
  - In this instance, we have a *home page* and an *about page*, and with routes, we can designate the web path to each
- Example:

```python
from flask import Blueprint, render_template

blueprint = flask.Blueprint("home", __name__, template_folder="templates")

@blueprint.route("/")
def index():
	return render_template("home/index.html")


@blueprint.route("/about")
def about():
	return render_template("home/about.html")
```

- Create flask app, and organize it to handle blueprints
- Example:

```python
from flask import Flask

app = Flask(__name__)

def main():
	register_blueprints()
	app.run(debug=True)


def register_blueprints():
	from views import view_name

	app.register_blueprint(views.view_name.blueprint)


if __name__ == "__main__":
	main()
```

- Now that the main flask app is setup, we can run it and the web server should run with no issues
- Run the program: `python3 app.py`


### Tips

- There are creative ways to use routes, for example, if you want to have a quick way to reach an episode number of a podcast site you run, maybe you want users to be able to reach the episode quickly like this: `http://example.com/4`. In this case, we want to see the 4th episode, so how do we handle that to where the URL doesn't accept strings?
- We will make an example blueprint

```python
# blueprint code above

@blueprint.route("<int: episode>")
def episodes(episode: int):
	return render_template("/episode/{}".format(episode), episode=episode)
```

- Notice that while rendering the template, the function is passing the variable `episode`. This is something that can then be used by the front end to use that variable through interpolation using brackets like this: `{{ variable }}` 
- Example:

```jinja
{% extends "shared/_layout.html" %}

{% block title %}
Episode {{ episode }}
{% endblock %}

{% block main_content %}
Welcome to Episode {{ episode }}!
{% endblock %}
```

## Advanced Routing with GET and POST
*Working with forms via routing*

- In some instances, sites will have forms that require users to fill out information, such as registering for a site. To do this, the end user will first need to GET the page where the form resides, then POST their information to the back end.
- Example:

```python
@blueprint.route("/account/register", methods=["GET"])
def register_get():
	return render_template("/account/register")

@blueprint.route("/account/register", methods=["POST"])
def register_post():
	return render_template("/account/register")
```

## Bootstrap
*Work with Bootstrap and front-end CSS*


### Grid Layout

- A great thing about Bootstrap is built-in plugins that can be used, we can use grids, buttons, forms and more
- Let's start with grids, every grid as a rule, has 12 columns per row
- There are also three different size modifiers, `lg`, `md`, and `sm`. These identifiers are keywords that causes "collapsing" when shrinking a page on your browser. This means that if a column has a `lg` identifier, it will collapse more quickly and stack on the page, while the `sm` break down only after the page size is small
- *Note:* You have to use the class `container`, `row`, and `col` for bootstrap to recognize your grid layout
- Example:

```html
<div class="container">
	<div class="row">
		<div class="col-md-8">col-md-8</div>
		<div class="col-md-4">col-md-4</div>
	</div>
	<div class="row">
		<div class="col-md-4">col-md-4</div>
		<div class="col-md-4">col-md-4</div>
		<div class="col-md-4">col-md-4</div>
	</div>
	<div class="row">
		<div class="col-sm-6">col-sm-4</div>
		<div class="col-sm-6">col-sm-4</div>
	</div>
	<div class="row">
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
		<div class="col-sm-1">col-sm-1</div>
	</div>
```


*Still in progress* -DV
