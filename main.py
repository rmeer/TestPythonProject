from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first-parameter">First Parameter:</label>
            <input id="first-parameter" type="text" name="first_parameter" />

            <label for="second-parameter">Second Parameter:</label>
            <input id="second-parameter" type="text" name="second_parameter" />
            <input type="submit" />

        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_parameter = request.form['first_parameter']
    second_parameter = request.form['second_parameter']
    return '<h1>' + first_parameter + ' ' + second_parameter + '</h1>'


app.run()