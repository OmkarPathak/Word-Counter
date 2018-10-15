from wordcounter import WordCounter
import argparse, sys

parser = argparse.ArgumentParser(description='Process some file text.')

# usage example: python main_wordcount.py --clf in.txt
if __name__ == '__main__':

    parser.add_argument("--clf", help="count number of words in specified file", type=str)
    args = parser.parse_args()
    if args.clf:
        data = ''
        try:
            with open(args.clf, 'r') as f:
                data = f.read().replace('\n', ' ')
        except Exception as e:
            print("Some error happened,please try again ", str(e))
            sys.exit(0)
        word_counter = WordCounter(data)
        print(word_counter.get_word_count())
