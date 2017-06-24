from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="POST">
            <label for="first_name">First Name:</label>
            <input id="first_name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

time_form = """
<style>
    .error {{ color: red; }}
</style>
<h1>Validate Time</h1>
<form action="/validate-time" method='POST'>
    <label>Hours (24-hour format)
        <input name="hours" type="text" value='{hours}' />
    </label>
    <p class="error">{hours_error}</p>
    <label>Minutes
        <input name="minutes" type="text" value='{minutes}' />
    </label>
    <p class="error">{minutes_error}</p>
    <input type="submit" value="Convert" />
</form>
"""

@app.route("/validate-time")
def display_time_form():
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')

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
        return time_form.format(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

@app.route("/valid-time")
def valid_time():
    time = request.args.get('time')
    return '<h1>Time at the tome: {0}</h1>'.format(time)
app.run()