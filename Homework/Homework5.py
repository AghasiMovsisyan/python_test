#1

'''

def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])



if is_palindrome((input('Enter a text: '))):
    print('Yes')
else:
    print('No')

'''


#2

'''

def guesser(start,stop,step = 0):
    if step == 0:
        while True:
            command = input('Think of a number between 1 and 999. input 0 once you are ready.')
            if command == '0':
                break

    if step < 10:
        step += 1
        guess = (start + stop) // 2
        print(f'My guess number {step}: {guess}')
        hint = input()
        if hint == '0':
            print(f'I guessed in {step} steps.')
        elif hint == '-1':
            guesser(start,guess - 1,stop)
        elif hint == '-1':
            guesser(guess + 1,stop,step)
        else:
            print('I cold not guess in 10 steps,which means you have cheated.')

guesser(start = 1,stop = 999)

'''

import Module

print(Module.print_something())


