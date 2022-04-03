'Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

'Examples
'pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    splitted_text = text.split(' ')
    result = ' '
    for word in splitted_text:
        if word in '!.%&?':
            result = result + word
        else:
            result = result + (word[1:] + word[0] + "ay") + " "
    return result.strip(' ')
