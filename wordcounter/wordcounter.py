
import argparse,sys

class WordCounter(object):
    def __init__(self, sentence, delimiter=None):
        '''
            :param sentence: Sequence of words or a single word
        '''
        self._sentence = sentence.split(delimiter)

    def __eq__(self, other):
        '''
            Checks if two WordCounter objects have same number of words
        '''
        if not isinstance(other, type(self)):
            return 'Class should be of type WordCounter and not ' + str(type(other))
        return len(self._sentence) == len(other._sentence)

    def __lt__(self, other):
        '''
            Checks if current WordCouter object has lesser number of 
            words than other WordCounter object
        '''
        if not isinstance(other, type(self)):
            return 'Class should be of type WordCounter and not ' + str(type(other))
        return len(self._sentence) < len(other._sentence)

    def __gt__(self, other):
        '''
            Checks if current WordCouter object has greater number of 
            words than other WordCounter object
        '''
        if not isinstance(other, type(self)):
            return 'Class should be of type WordCounter and not ' + str(type(other))
        return len(self._sentence) > len(other._sentence)

    def get_word_count(self):
        '''
            :return: total count of words in the sentence
        '''
        return len(self._sentence)

    def count(self, word, ignore_case=True):
        '''
            :param word: Word whose occurance(frequency) is to calculated
        '''
        if ignore_case:
            all_lower_words = [word.lower() for word in self._sentence]
            return all_lower_words.count(word)
        return self._sentence.count(word)

    def get_word_frequencies(self, ignore_case=True):
        '''
            :return: the tuple of word and count of each word in the sentence
        '''
        temp_dic = {}
        if ignore_case:
            for char in self._sentence:
                keys = temp_dic.keys()
                if char in keys:
                    temp_dic[char.lower()] += 1
                else:
                    temp_dic[char.lower()] = 1
        else:
            for char in self._sentence:
                keys = temp_dic.keys()
                if char in keys:
                    temp_dic[char] += 1
                else:
                    temp_dic[char] = 1
        return temp_dic

    def most_common(self, count):
        # TODO
        pass


def main():
    parser = argparse.ArgumentParser(description='Process some file text.')
    parser.add_argument("--f", help="count number of words in specified file", type=str)
    args = parser.parse_args()
    if args.f:
        data = ''
        try:
            with open(args.f, 'r') as f:
                data = f.read().replace('\n', ' ')
        except Exception as e:
            print("Some error happened,please try again ", str(e))
            sys.exit(0)
        word_counter = WordCounter(data)
        print(word_counter.get_word_count())


if __name__ == '__main__':
    main()

