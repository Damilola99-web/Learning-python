print("Welcome to the word replacement program. \nYou'll be asked to enter the word, word to be replaced, and the the rplacement word. \nSo let's get started...")
word = input("Enter the word: ")
word_to_be_replaced = input("Enter the word to be replaced: ")
replacement = input("Enter the replacement word: ")

print(word.replace(word_to_be_replaced, replacement))
