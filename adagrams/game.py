from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def available_letters():

    available_letters = []

    for letter, quantity in LETTER_POOL.items():
        available_letters.extend(([letter] * quantity))
    return available_letters
    

def draw_letters():

    letters_list = available_letters()
    letters = []
    
    while len(letters) < 10:
        i = randint(1, len(letters_list)-1)
        letters.append(letters_list[i])
        letters_list.pop(i)

    return letters

def making_words_into_list(words):

    usable_words = []

    for letter in words:
        usable_words.append(letter.upper())
    
    return usable_words

def uses_available_letters(word, letter_bank):

    split_word = making_words_into_list(word)

    for letter in split_word:
        if (letter not in letter_bank or 
            split_word.count(letter)>letter_bank.count(letter)):
            is_valid = False
        else:
            is_valid = True

    return is_valid

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
