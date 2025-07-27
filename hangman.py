import random

# List of words for the game
words = ['PYTHON', 'HANGMAN', 'DEVELOPER', 'PROGRAM', 'CODING']
max_attempts = 6

# Hangman graphics for each wrong attempt
hangman_graphics = [
    '''
     _____
    |     |
    |     
    |    
    |     
    |    
   _|_
    ''',
    '''
     _____
    |     |
    |     O
    |    
    |     
    |    
   _|_
    ''',
    '''
     _____
    |     |
    |     O
    |     |
    |     
    |    
   _|_
    ''',
    '''
     _____
    |     |
    |     O
    |    /|
    |     
    |    
   _|_
    ''',
    '''
     _____
    |     |
    |     O
    |    /|\\
    |     
    |    
   _|_
    ''',
    '''
     _____
    |     |
    |     O
    |    /|\\
    |    / 
    |    
   _|_
    ''',
    '''
     _____
    |     |
    |     O
    |    /|\\
    |    / \\
    |    
   _|_
    '''
]

def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def play_hangman():
    secret_word = random.choice(words)
    guesses = []
    attempts = 0
    
    print("Welcome to Hangman!")
    
    while attempts < max_attempts:
        print(hangman_graphics[attempts])
        print(display_word(secret_word, guesses))
        
        guess = input("Guess a letter: ").upper()
        
        if guess in guesses:
            print("You already guessed that!")
            continue
            
        guesses.append(guess)
        
        if guess not in secret_word:
            attempts += 1
            print("Wrong guess!")
            
        if all(letter in guesses for letter in secret_word):
            print("Congratulations! You won!")
            break
            
    else:
        print(hangman_graphics[max_attempts])
        print(f"Game over! The word was: {secret_word}")

# Start the game
if __name__ == "__main__":
    play_hangman()
