# Write a program that automatically converts English text to Morse code and vice versa:
eng_to_morse_dict = {'A': '.-', 'B': '-...',
                     'C': '-.-.', 'D': '-..', 'E': '.',
                     'F': '..-.', 'G': '--.', 'H': '....',
                     'I': '..', 'J': '.---', 'K': '-.-',
                     'L': '.-..', 'M': '--', 'N': '-.',
                     'O': '---', 'P': '.--.', 'Q': '--.-',
                     'R': '.-.', 'S': '...', 'T': '-',
                     'U': '..-', 'V': '...-', 'W': '.--',
                     'X': '-..-', 'Y': '-.--', 'Z': '--..',
                     '1': '.----', '2': '..---', '3': '...--',
                     '4': '....-', '5': '.....', '6': '-....',
                     '7': '--...', '8': '---..', '9': '----.',
                     '0': '-----', ', ': '--..--', '.': '.-.-.-',
                     '?': '..--..', '/': '-..-.', '-': '-....-',
                     '(': '-.--.', ')': '-.--.-', ' ':' ' }
morse_to_eng_dict = {value: key for key, value in eng_to_morse_dict.items()}


def translator(text_to_translate, direction='to_morse'):
    if direction == 'to_eng':
        translation = ''.join([morse_to_eng_dict[letter] for letter in text_to_translate])
        return translation
    elif direction == 'to_morse':
        translation = [eng_to_morse_dict[letter.upper()] for letter in text_to_translate]
        return translation
    else:
        return "Please chose a valid translation direction: 'to_morse' or 'to_eng'. (default value: 'to_morse)'"

'''
# tests
print(translator('hello'))
print(translator(['....', '.', '.-..', '.-..', '---'], direction='to_eng'))
print(translator('The quick brown fox jumped over the lazy dog.', direction='sjahsdh'))
'''

while True:
    print(translator(input('Enter text to translate: ')))
