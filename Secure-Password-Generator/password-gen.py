import argparse
import random

parser = argparse.ArgumentParser(prog='xkcdpwgen', description='Generate a secure, memorable password using the XKCD method')
parser.add_argument("-w", "--words", type=int, default=4, help='include WORDS words in the password (default=4)')
parser.add_argument("-c", "--caps", type=int, default=0, help='capitalize the first letter of CAPS random words (default=0)')
parser.add_argument("-n", "--numbers", type=int, default=0, help='insert NUMBERS random numbers randomly in the password (default=0)')
parser.add_argument("-s", "--symbols", type=int, default=0, help='insert SYMBOLS random symbols randomly in the password (default=0)')
args = parser.parse_args()

def choose_word(file_name):
    with open(file_name) as word_file:
        return list(set(word.strip() for word in word_file))
        
def random_words(n, words):
    return "".join(random.choice(words) for _ in range(n))
    
def main(file_name):
    words = choose_word(file_name)
    n = int(args.words)
    print(random_words(n, words))
  
# Here is where you can add whatever dictionary you choose. I used corncob_lowercase.txt
if __name__ == "__main__":
    file_name = "corncob_lowercase.txt"
    main(file_name)
