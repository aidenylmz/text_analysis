from nltk.tokenize import word_tokenize
from nltk import pos_tag

s = 'There is a problem with Traffic Light'
tokens = word_tokenize(s)  # Generate list of tokens
tokens_pos = pos_tag(tokens)
print(tokens_pos)
