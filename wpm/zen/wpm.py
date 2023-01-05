import os
import random
import time


ZEN_FILE = "zen.txt"

def formula(original_text, typed_text, duration):

    errors = len(original_text)

    for i, j in zip(original_text, typed_text):
        if i == j:
            errors -= 1


    score = 60 * (len(original_text) / 5 - errors / duration) / duration
    accuracy = 100 - errors * 100 // len(original_text)

    return {
        'score': score,
        'accuracy': accuracy,
    }

def collect_data(text):
    print(text)
    start = time.time()
    typed = input()
    duration = time.time() - start
    return typed, duration



def get_a_sentence():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    zen_file_path = os.path.join(directory, ZEN_FILE)

    with open('zen.txt') as f:
        return random.choice(f.readlines()).rstrip()

def main():
    sentence = get_a_sentence()
    typed, duration = collect_data(sentence)
    result = formula(sentence,typed,duration)
    print('Your score is {score}. Accuracy is {accuracy} %.'.format(**result))

if __name__ == '__main__':
    main()







