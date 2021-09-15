"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game', methods = ['POST'])
def show_madlib_form():
    """get user response to game proposition"""
    answer = request.form.get("yes_game")
    
    if answer == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")
    
@app.route('/madlib', methods = ['POST'])
def show_madlib():
    """get user input for madlib"""
    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    noun_2 = request.form.get("noun_2")
    plural_noun = request.form.get("plural_noun")
    poem = choice(["madlib.html", "mad_lib2.html"])

    return render_template(poem, person = person, color=color, noun=noun, adjective=adjective, noun_2=noun_2, plural_noun=plural_noun)
if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
