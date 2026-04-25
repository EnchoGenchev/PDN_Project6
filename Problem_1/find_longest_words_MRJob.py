from mrjob.job import MRJob

class MRLongestWord(MRJob):

    def mapper(self, _, line):
        #string with all the characters
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        # Replace hyphens and em-dashes with spaces
        line = line.replace('-', ' ').replace('—', ' ')
        
        chunks = line.split()
        
        for chunk in chunks:
            raw_chunk = chunk.lower()
            
            #only keep letters
            word = "".join([char for char in raw_chunk if char in alphabet])
            
            #make sure word starts with valid char
            if word and word[0] in alphabet:
                yield word[0], word

    def reducer(self, letter, words):
        max_length = 0
        longest_words = set()

        for word in words:
            word_len = len(word)
            if word_len > max_length:
                max_length = word_len
                longest_words = {word}
            elif word_len == max_length:
                longest_words.add(word)

        yield letter, sorted(list(longest_words))

if __name__ == '__main__':
    MRLongestWord.run()