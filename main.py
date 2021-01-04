# %%
# from helpers.extensions import load_multiple_corpus_files
from nltk.corpus.reader.tagged import TaggedCorpusReader
import nltk
from helpers.extensions import count_keys_by_value, lower_files, sort_dict_by_value, keys_by_value, change_files_with_unknown_words, replace_dict_by_unknown

# %%
# Lower cases the files and saves it to another location
# lower_files('docs\\brown_hw\\Train\\', 'docs\\brown_hw_lowercase\\Train\\')
# lower_files('docs\\brown_hw\\Test\\', 'docs\\brown_hw_lowercase\\Test\\')

# load_multiple_corpus_files('docs\\brown_hw\\Train\\')
# load_multiple_corpus_files('docs\\brown_hw\\Test\\')

# %%
# TaggedCorpusReader for train set
train_root = 'docs\\brown_hw_lowercase\\Train'
train_reader = TaggedCorpusReader(train_root, '.*')
# %%
train_words = train_reader.words()
# %%
train_word_counts = nltk.FreqDist(train_words)
# %%
# Words of train set that occurs only once
train_word_counts_1 = keys_by_value(train_word_counts)
# %%
# Words with tags of train set
tagged_words_with_unk = [list(x) for x in train_reader.tagged_words()]
# %%
# Makes words 'UNK' whose counts are one
for index, tagged_word in enumerate(tagged_words_with_unk):
    if tagged_word[0] in train_word_counts_1.keys():
        tagged_words_with_unk[index][0] = 'UNK'
# %%
# Computes tag frequencies and put them into dictionary
tag_frequency = {}
for index, tagged_word in enumerate(tagged_words_with_unk):
    try:
        tag_frequency[tagged_word[1]] += 1
    except KeyError:
        tag_frequency[tagged_word[1]] = 1

# %%
# Sorted tag frequency dictionary
tag_frequency = sort_dict_by_value(tag_frequency)
# %%
