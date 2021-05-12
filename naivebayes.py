import nltk
from nltk.tokenize import word_tokenize
import random
import common
training_set = ([(i, 'pos') for i in common.positive] + [(i, 'neg') for i in common.negative])
random.shuffle(training_set)
all_words = set(word for passage in training_set for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in training_set]
classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features(5)

