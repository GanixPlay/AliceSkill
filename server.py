from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('alogritmika.html')


def main():
    app.run()


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
