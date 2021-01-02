# %%
# from helpers.extensions import load_multiple_corpus_files
from nltk.corpus.reader.tagged import TaggedCorpusReader
from collections import Counter
import nltk
from helpers.extensions import lower_files

# %%
# lower_files('./venv/nltk_data/corpora/brown_hw/Train/')
# lower_files('./venv/nltk_data/corpora/brown_hw/Test/')

# %%
train_root = './venv/nltk_data/corpora/brown_hw/Train/'
train_reader = TaggedCorpusReader(train_root, '.*')

# %%
train_words = train_reader.words()

# %%
train_word_counts = Counter(train_words)

# %%
