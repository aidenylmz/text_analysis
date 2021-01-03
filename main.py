# %%
# from helpers.extensions import load_multiple_corpus_files
from nltk.corpus.reader.tagged import TaggedCorpusReader
import nltk
import json
from helpers.extensions import lower_files

# %%
lower_files('docs\\brown_hw\\Train\\', 'docs\\brown_hw_lowercase\\Train\\')
lower_files('docs\\brown_hw\\Test\\', 'docs\\brown_hw_lowercase\\Test\\')

# load_multiple_corpus_files('docs\\brown_hw\\Train\\')
# load_multiple_corpus_files('docs\\brown_hw\\Test\\')

# %%
train_root = 'docs\\brown_hw\\Train'
train_reader = TaggedCorpusReader(train_root, '.*')
# %%
train_words = train_reader.words()
# %%
train_word_counts = nltk.FreqDist(train_words)
# %%
with open('docs/train_word_counts.json', 'w') as fp:
    json.dump(train_word_counts, fp)
# %%
lower_all_files('docs\\brown_hw\\Train')

# %%
