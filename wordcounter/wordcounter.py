class WordCounter(object):
    def __init__(self, sentence, delimiter=' '):
        '''
            :param sentence: Sequence of words or a single word
        '''
        self._sentence = sentence.split(delimiter)

    def __eq__(self, other):
        '''
            Checks if two WordCounter objects have same number of words
        '''
        return len(self._sentence) == len(other.sentence)

    def __lt__(self, other):
        '''
            Checks if current WordCouter object has lesser number of 
            words than other WordCounter object
        '''
        return len(self._sentence) < len(other.sentence)

    def __gt__(self, other):
        '''
            Checks if current WordCouter object has greater number of 
            words than other WordCounter object
        '''
        return len(self._sentence) > len(other.sentence)

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
    

if __name__ == '__main__':
    word_counter = WordCounter('The quick brown fox jumps over the lazy dog')
    # word_counter2 = WordCounter('the quick brown fox jumps over the lazy dog')
    # print(word_counter == word_counter2)
    print(word_counter.get_word_count())
    print(word_counter.count('the'))
    print(word_counter.get_word_frequencies())
