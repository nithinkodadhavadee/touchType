from nltk.corpus import gutenberg;
from pynput.keyboard import Key, Listener;
import random;

def on_release(key):
    print(key);
    if key == 'q':
        exit();
    elif key == Key.enter:
        print('next');

fileCount = len(gutenberg.fileids());
fileName = gutenberg.fileids();

fileName =  gutenberg.sents(random.choice(fileName));

print(' '.join(fileName[0]),"\n");

while 1:
    sentence = random.randrange(0,len(fileName));
    sentence = ' '.join(fileName[sentence]);
    print(sentence);

    with Listener(
            on_release=on_release) as listener:
        listener.join()
