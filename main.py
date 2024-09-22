from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>hello i am paragraph</p>'
            '<img src="https://media1.giphy.com/media/uUP7F5A1rQR9uKls9P/giphy.webp?cid=6c09b952ozo94gdjzj1z0wd7ff0wtip40qhfi05cb2k7235w&ep=v1_gifs_trending&rid=giphy.webp&ct=g">')


def make_bold(func):
    def wrapper_fun():
        return f"<b>{func()}</b>"
    return wrapper_fun


def make_underlined(func):
    def wrapper_fun():
        return f"<u>{func()}</u>"
    return wrapper_fun


def make_emphasis(func):
    def wrapper_fun():
        return f"<em>{func()}</em>"
    return wrapper_fun


@app.route("/hii")
@make_bold
@make_underlined
@make_emphasis
def say_hii():
    return 'Hii!'


@app.route("/username/<name>")
def greet(name):
    return f"hello {name + '12'}"


if __name__ == "__main__":
    app.run(debug=True)

