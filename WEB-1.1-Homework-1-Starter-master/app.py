import random
from flask import Flask

app = Flask(__name__)
# Hello, World! (Tutorial)
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

# Your User's Favorite Animal (Tutorial)
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favourite animal"""
    return f'Wow, {users_animal} is my favorite animal, too!'

# Your User's Favorite Dessert
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favourite dessert"""
    return f'How did you know I like {users_dessert}?'

# Mad Libs
@app.route('/madlibs/<users_adjective>/<users_noun>')
def story(users_adjective, users_noun):
    """Display a story to the user that changes based on the adjective and noun they provided"""
    return f'A {users_adjective} cloud was released when herd of elephants trampled over the {users_noun}!'

# Multiply 2 Numbers
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """display the product of multiplying 2 numbers to the user that changes based on the numbers they provide
    the numbers must be numbers"""
    
    if number1.isdigit() is False or number2.isdigit() is False: 
        return 'Invalid inputs. Please try again by entering 2 numbers!'
     
    return f'{number1} times {number2} is ' + str(int(number1) * int(number2))

# Say N Times
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if word.isdigit() is True or n.isdigit() is False: 
        return 'Invalid inputs. Please try again by entering a word and a number!'

    string = ""
    for i in range(int(n)):
        string += word + " "
    return f'{string}'

# Dice Game
@app.route('/dicegame')
def dicegame():

    roll = random.randint(1, 6)
    if roll == 6:
        return 'You rolled a 6. You won!'

    return f'You rolled a {roll}. You lost!'


# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)