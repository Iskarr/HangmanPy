# This is a guesss the number game
import random, re

# print("Hello, What is your name?")
# name = input()
# print("Well, " + name + ", Welcome to hangmanPy!")

secretWords = ["Tom", "Bat", "Cat", "Batman"]

word = random.choice(secretWords)

print(word)


def checkLetter():
    guess = input()
    if guess in word:
        print("That letter is in the word.")
        print(word.translate({ord(guess): None}))
    else:
        print("That letter isnt in the word, try again!")


checkLetter()

# secretNumber = random.randint(1, 20)
# for guessesTaken in range(1, 7):
#     print("Take a guess.")
#     guess = int(input())

#     if guess < secretNumber:
#         print("Your guess is too low.")
#     elif guess > secretNumber:
#         ("Your guess is too high.")
#     else:
#         break


# if guess == secretLetter:
#     print(
#         "Good Job!"
#         + name
#         + " You guessed my number in "
#         + str(guessesTaken)
#         + " guesses."
#     )
# else:
#     print("Nope. The number I was thinking of was " + str(secretNumber))

# print("You took " + str(guessesTaken) + " guesses.")
