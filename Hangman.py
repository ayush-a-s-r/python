import random
from words import wordsfor_hangman

def get_word():
    word = random.choice(wordsfor_hangman)
    return word.upper()
    # using upper case so that its easy read

def play(word):
    word_completion = "_" * len(word)
    # '_' used to display unguessed word

    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # total no. of tries [6 for head,legs,arms,body/torso]

    print("Let's play Hangman!")
    print(display_hangman(tries))
    #calling function to show hangman

    print(word_completion)
    # calling function to display no. of '_' according to length of word

    print("\n")
    while not guessed and tries > 0:
        # guess is true and tries are greater than 0

        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            # to check if input word is a single character & its an alphabet

            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                # if you enter same letter twice

            elif guess not in word:
                print(guess, "is not in the word.")
                # if character doesnt match the letter, above msg is shown

                tries -= 1
                # wrong guess takes 1 guess away

                guessed_letters.append(guess)
                # guess gets appended to guessed letters
            else:
                print("Good job,", guess, "is in the word!")
                # word has been guessed right

                guessed_letters.append(guess)
                # guess gets appended to guessed letters

                word_as_list = list(word_completion)
                # new list created to show user that all guesses r complete--string converted to list--for indexing
                # new list can be called as 'word as list'
                # now we use list comprehension to find all the index position where the guesses r in a word

                indices = [i for i, letter in enumerate(word) if letter == guess]
                # calling to find index 'i' & 'letter' at the index at each iteration
                # append 'i' to list[word], to check if corresponding letter is the correct guess

                for index in indices:
                    word_as_list[index] = guess
                    # each '_' replaced bu guess

                word_completion = "".join(word_as_list)
                # empty string used to store the converted list back into string

                if "_" not in word_completion:
                    guessed = True
                    # here we check if the word is complete or the last guess completes the word

        elif len(guess) == len(word) and guess.isalpha():
            # to check if input guesses matches the word
            
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        # while loop works till the word is guessed or user runs out of tries
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
