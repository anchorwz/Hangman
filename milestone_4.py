import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        # self.word_list = ['apple', 'banana', 'orange', 'grape', 'peach']
        random_ind = random.randint(0, 4)
        self.word = word_list[random_ind] 
        self.word = 'banana'
        print(self.word)
        self.word_guessed = [ '_'*len(each) for each in self.word]
        self.num_letters = len([ one for one, two in zip(self.word, self.word_guessed) if one!= two ])
        self.num_lives = 6
        self.list_of_guesses = []
       

    def check_guess(self, guess):
        tolow_guess = guess.lower()
        if tolow_guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for one in self.word:
                if one == tolow_guess:
                    ind = self.word.index(one)
                    self.word_guessed[ind] = one
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')


    def ask_for_input(self):

        while True:
            guess = input('Please enter a letter')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character')
                continue
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                continue
            
            self.check_guess(guess) 
            self.list_of_guesses.append(guess)
            break



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print('You lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
            continue
        if num_lives !=0 and game.num_letters <=0:
            print('Congratulations. You won the game!')
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'grape', 'peach']
    play_game(word_list)

