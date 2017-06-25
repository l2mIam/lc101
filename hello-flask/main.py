from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template("hello_greating.html")
    return template.render(name=first_name)

time_form = """
"""

@app.route("/validate-time")
def display_time_form():
    template = jinja_env.get_template("validate_time_form.html")
    return template.render(hours='', hours_error='', minutes='', minutes_error='')

@app.route("/validate-time", methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour outside range (0-23)'
            hours = ''
    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minute outside range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        # success
        min_buff = ''
        if minutes < 10:
            min_buff = 0
        time = str(hours) + ":" + str(min_buff) + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        template = jinja_env.get_template("validate_time_form.html")
        return template.render(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/valid-time")
def valid_time():
    the_time = request.args.get('time')
    template = jinja_env.get_template("valid_time.html")
    return template.render(time=the_time)
app.run()