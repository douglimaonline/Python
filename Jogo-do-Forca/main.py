import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
print ("\n")
game_is_finished = False
lives = len(stages) - 1
guess_try = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
print ("\n")

while not game_is_finished:
    guess = input("Escolha uma letra: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"A letra {guess} já foi escolhida.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess in guess_try:
      print(f"A letra {guess} já foi escolhida.")

      
    elif guess not in chosen_word:
      guess_try.append(guess)
      print(f"A letra {guess} não está na palavra. Você perdeu uma vida.")
      lives -= 1
          
  
    if lives == 0:
      game_is_finished = True
      print("Você Perdeu.")
      print (f"A palavra era {chosen_word}")
    
    if not "_" in display:
        game_is_finished = True
        print("Você Ganhou")

    print(stages[lives])