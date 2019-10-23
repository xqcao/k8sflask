from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello_page.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
