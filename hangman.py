import random
from hangman_words import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
chosen_word = random.choice(word_list)
lives = 6
guesses_made = []
display = []

for letter in chosen_word:
    display.append('_')

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

while '_' in display:
    guess = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in display:
        print('wrong letter')
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print('You lose')
            print(f'The solution was {chosen_word}')
            break
    if guess in guesses_made:
        print(f"{guess}? I think you've already tried this")
        continue
    guesses_made.append(guess)

    print(f' '.join(display))
if '_' not in display:
    print('You win')
