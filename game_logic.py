class HangmanGame:
    def __init__(self):
        self.secret_word = ""
        self.clue = ""
        self.guesses = set()
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        self.previous_attempts = self.max_attempts  # New attribute to track the previous number of attempts

    def set_word_and_clue(self, word, clue):
        self.secret_word = word.lower()
        self.clue = clue
        self.guesses.clear()
        self.attempts_left = self.max_attempts
        self.previous_attempts = self.max_attempts  # Reset on setting a new word

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter not in self.guesses:
            self.previous_attempts = self.attempts_left  # Update previous attempts before changing the current attempts
            self.guesses.add(letter)
            if letter not in self.secret_word:
                self.attempts_left -= 1
        return self.attempts_left > 0 or self.is_word_guessed()

    def is_word_guessed(self):
        return all(letter in self.guesses for letter in self.secret_word if letter.isalpha())

    def get_display_word(self):
        return ''.join(letter if letter in self.guesses else '_' for letter in self.secret_word)
