from flask import Flask, render_template, request, redirect, url_for
from game_logic import HangmanGame

app = Flask(__name__)
game = HangmanGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_word', methods=['GET', 'POST'])
def set_word():
    if request.method == 'POST':
        word = request.form['word']
        clue = request.form['clue']
        game.set_word_and_clue(word, clue)
        return redirect(url_for('guess'))
    return render_template('set_word.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        if 'letter' in request.form:
            letter = request.form['letter']
            game.guess_letter(letter)
            if game.is_word_guessed():
                return render_template('win.html', word=game.secret_word, won=True)
            elif game.attempts_left <= 0:
                return render_template('win.html', word=game.secret_word, won=False)
        elif 'word_guess' in request.form:
            word_guess = request.form['word_guess']
            if word_guess.lower() == game.secret_word:
                return render_template('win.html', word=game.secret_word, won=True)
            else:
                return render_template('win.html', word=game.secret_word, won=False)
    return render_template('guess.html', display_word=game.get_display_word(), attempts_left=game.attempts_left, clue=game.clue, previous_attempts=game.previous_attempts)

@app.route('/win')
def win():
    return render_template('win.html', word=game.secret_word, won=game.is_word_guessed())

if __name__ == '__main__':
    app.run(debug=True)
