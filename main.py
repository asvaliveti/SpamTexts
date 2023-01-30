import os
from time import sleep

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
        length = len(text)
        wordsArr = []
        for i in range(length):
            words = text[i].split()
            wordsArr = wordsArr + words
        print(wordsArr)
    return wordsArr

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    words = get_words('words.txt')
    for i in range(100):
        word = ""
        for i in range(len(words)):
            word = words[i]
            print(word)
            send_message("+15713535352", word)
