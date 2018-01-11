from nltk import word_tokenize, sent_tokenize, pos_tag
from nltk.book import *

sentences = sent_tokenize("Google is one of the best companies in the world.I constantly google myself to see what I'm up to.")
nouns = ['NN', 'NNS', 'NNP', 'NNPS']

print(sentences)