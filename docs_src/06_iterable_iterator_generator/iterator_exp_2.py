# Example for iterator and generator

class SentIter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        else:
            return_val = self.words[self.index]
            self.index += 1
            return return_val


corpus = "Tub likes Blue Cheese"
words = SentIter(corpus)
for word in words:
    print(word)
# Output: Tub
# Output: likes
# Output: Blue
# Output: Cheese


def iter_sent(sentence):
    for word in sentence.split():
        yield word


words = iter_sent(corpus)
for word in words:
    print(word)