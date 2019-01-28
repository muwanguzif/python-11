def vowelify(word):
    # well -> wll e
    # cool -> cl oo
    consonants = ''
    vowels = ''
    for index in range(0, len(word)):
        letter = word[index]
        if letter in 'aeiou':
            vowels += letter
        else:
            consonants += letter

    return consonants + ' ' + vowels


while True:
    word = input('Enter a word: ')
    if word == '.exit':
        break
    print('vowelify:', vowelify(word)) # -> wrdo`