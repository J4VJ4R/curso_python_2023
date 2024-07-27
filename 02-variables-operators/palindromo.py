word = input("Type your word: ")

#Changing word to uppercase
word = word.lower()

#Replace spaces
new_word = word.replace(" ", "")

reverse_word = new_word[::-1]

if new_word == reverse_word:
  print(f"The word: {word} Is palindrome")
else:
  print(f"The word: {word} Is not palindrome :(")