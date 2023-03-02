# Shijang Lin PSID: 2018904

# Lab 8.10

def is_palindrome(word):
    new_word = word.replace(' ', '')
    reverse = ''
    result = False
    for i in new_word:
        reverse = i + reverse
    if reverse == new_word:
        result = True
    return result


sentence = input()
answer = is_palindrome(sentence)
if answer:
    print(f'{sentence} is a palindrome')
else:
    print(f'{sentence} is not a palindrome')
