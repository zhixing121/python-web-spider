from nltk import word_tokenize
from nltk import Text
from nltk.book import *

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
print(text)

print(text6)