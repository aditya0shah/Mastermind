# to use on a non-color supported terminal remove colorama library and Fore.color in print statements

import random 
from colorama import Fore

letters = ["A", "B", "C", "D", "E", "F"]
length = 4

def main():
  list_code = create_code(length)
  secret_code = "".join(list_code)

  guess_counter = 0
  guess = ""
  list_guess = ""
  while guess_counter < 10 and guess != secret_code:
    list_guess = get_code()
    guess = "".join(list_guess)
    result = check_code(secret_code, guess)
    guess_counter+= 1
  

  if guess == secret_code:
    print("You win!")
  else:
    print("Sorry, you lost. The corect code was", secret_code)

#creating secret_code
def create_code(length):
  letters_copy = letters.copy()
  code_word = ""
  for i in range(length):
    letter = random.choice(letters_copy)
    letters_copy.remove(letter)
    code_word = code_word + letter
  code = list(code_word)
  return code

#get input
def get_code():
  guess_code = input("Guess the 4 digit code (abcd): ").upper()
  user_code = list(guess_code)
  if len(user_code) != length:
    print("Must enter", length, "letters")
    get_code()
  for i in range(len(guess_code)):
    if user_code[i] in letters: 
      continue
    else:
      print("invalid answer, choose between letters a, b, c, d, e, f")
      get_code()
      break
  return guess_code

#checking input
def check_code(secret_code, guess):
  white_counter = 0
  red_counter = 0
  win = False
  for i in range(len(guess)):
    if guess[i] == secret_code[i]:
      red_counter += 1
      continue
    elif guess[i] in secret_code:
      white_counter += 1
      continue
    else:
      continue
  print(Fore.RED + "R"*red_counter, end = " ")
  print(Fore.WHITE + "W"*white_counter, end=" ")
  print(Fore.WHITE + "")

  
  return white_counter, red_counter


main()
