from __future__ import division
import string

class nlp(object):
    def __init__(self):
        self.X = []
        self.uniques = []
        self.tf = []

    def fit(self, x, remove_stop_words=True,
                     porter_stemmer=Fale,
                     snowball_stemmer=False,
                     wordnet_stemmer=False):
        """
        X should be a string.  No unicode, no emoji...
        X will be one document, one string.
        """

        for p in string.punctuation:
            x = x.replace(p, '')

        self.X = [ word for word in x.lower().split() if x != '' ]

        if remove_stop_words:
            from stop_words import get_stop_words
            stop_words = get_stop_words('en')
            self.X = filter(lambda word: word not in stop_words, self.X)

        # ------- STEMMERS -------
        if porter_stemmer:
            from nltk.stem.porter import PorterStemmer

            porter = PorterStemmer()
            self.X = [ porter.stem(word) for word in self.X ]

        if snowball_stemmer:
            from nltk.stem.snowball import SnowballStemmer

            snowball = SnowballStemmer('english')
            self.X = [ snowball.stem(word) for word in self.X ]

        if wordnet_stemmer:
            from nltk.stem.wordnet import WordNetLemmatizer

            wordnet = WordNetLemmatizer()
            self.X = [ wordnet.lemmatize(word) for word in self.X ]


        self.uniques = list(set(self.X))

        self.doc_freq()

    def doc_freq(self):
        self.tf = [ self.X.count(word) / len(self.X) for word in self.uniques ]

    def plot(self, num_features=0):
        import matplotlib.pyplot as plt
        import numpy as np

        q = zip(self.uniques, self.tf)
        x = np.array(sorted(q, key=lambda x: x[1], reverse=True))

        if num_features:
            x = x[:num_features]

        plt.plot(x[:,1])
        plt.xticks(range(len(x[:,1])), x[:,0].tolist(), rotation='vertical')
        # plt.margins(0.2)
        plt.show()

    def remove_html(x):
        for place, l in enumerate(x):
            if '<' in x[place:] and '>' in x[place:]:
                x1 = x[place:].find('<')
                x2 = x[place:].find('>')

                if x1 < x2:
                    x = []

if __name__ == '__main__':
    pass
from NLP.nlp import nlp
a = nlp()

s = """Because the term "the" is so common, term frequency will tend to incorrectly emphasize documents which happen to use the word "the" more frequently, without giving enough weight to the more meaningful terms "brown" and "cow". The term "the" is not a good keyword to distinguish relevant and non-relevant documents and terms, unlike the less common words "brown" and "cow". Hence an inverse document frequency factor is incorporated which diminishes the weight of terms that occur very frequently in the document set and increases the weight of terms that occur rarely."""
a.fit(s)

























#
