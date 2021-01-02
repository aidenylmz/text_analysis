# %%
# from helpers.extensions import load_multiple_corpus_files
from nltk.corpus.reader.tagged import TaggedCorpusReader

# %%
root = './venv/nltk_data/corpora/brown_hw/Train/'
reader = TaggedCorpusReader(root, '.*')
