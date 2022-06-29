def game_instruction():
    print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "✔❌❌✔➕"  
"✔" Indicates that the letter at that position was guessed correctly

"➕" indicates that the letter at that position is in the hidden word, but in a different position

"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   \n""")

game_instruction()

def check_word():
  import random
  hidden_word = open("word_file.txt","r").read().splitlines()
  wordle = random.choice(hidden_word).lower()
  print(wordle) #to see the hidden word, remove in actual game
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word:")).lower() #force users to input 5 letters
    if guess == wordle:
      print("You guessed the word correctly! What a chad...")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) left \n")
      for char, word in zip(wordle, guess):
            if word in wordle and word in char:
                print(word + " ✔ ")
            elif word in wordle: #improvement: do not make duplicates show up, if letter has been guessed
                print(word + " ➕ ")
            else:
                print(word + " ❌ ")
      if attempt == 0:
        print("Try again next time loser KEKL")
        
check_word()
















