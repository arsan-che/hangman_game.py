import random


class Hangman:
    def __init__(self, word_list, num_lives=5, **kwargs): 
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [] 
        
    def check_guess(self, guess):
      guess = guess.lower()
      if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        for i, letter in enumerate(self.word):
          if letter == guess:
            self.word_guessed[i] = guess
            self.num_letters -= 1
        print(self.word_guessed)
      else:
          print(f"Sorry, {guess} is not in the word.")
          self.num_lives -= 1
          print(f"You have {self.num_lives} lives left.")