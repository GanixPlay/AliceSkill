from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        print(request.form.get('name'))
        print(request.form.get('radio'))
        print(request.form.getlist('alco'))
        return render_template('index.html')


def main():
    app.run('127.0.0.1', 8080)


if __name__ == '__main__':
    main()
