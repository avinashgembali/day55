from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def guess():
    return (f'<h1>guess an number between 0 and 9</h1>'
            f'<img width="300" height="300" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3N'
            f'jExMm02aWlucG13Y2ZwOWNjYXFrejJkc3IyMDZ3M2xrNWp5OXdlYzhnZCZlcD12MV9naWZzX3NlYXJjaC'
            f'ZjdD1n/Rs2QPsshsFI9zeT4Kn/giphy.webp">')


@app.route("/<int:guessed>")
def number_checker(guessed):
    choice = random.randint(0, 9)
    if guessed < choice:
        return ('<h1 style="color:red">too low !</h1>'
                '<img width="300" height="300"src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif guessed > choice:
        return ('<h1 style="color:blue">too high !!</h1>'
                '<img width="300" height="300"src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>')
    return ('<h1 style="color:blue">you got me correct!</h1>'
            '<img width="300" height="300" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
