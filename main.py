# %%
# from helpers.extensions import load_multiple_corpus_files
from nltk.corpus.reader.tagged import TaggedCorpusReader
import nltk
from helpers.extensions import count_keys_by_value, lower_files, sort_dict_by_value, keys_by_value, change_files_with_unknown_words, replace_dict_by_unknown

# %%
# lower_files('docs\\brown_hw\\Train\\', 'docs\\brown_hw_lowercase\\Train\\')
# lower_files('docs\\brown_hw\\Test\\', 'docs\\brown_hw_lowercase\\Test\\')

# load_multiple_corpus_files('docs\\brown_hw\\Train\\')
# load_multiple_corpus_files('docs\\brown_hw\\Test\\')

# %%
train_root = 'docs\\brown_hw_lowercase\\Train'
train_reader = TaggedCorpusReader(train_root, '.*')
# %%
train_words = train_reader.words()
# %%
train_word_counts = nltk.FreqDist(train_words)
# %%
# with open('docs/train_word_counts.json', 'w') as fp:
#     json.dump(train_word_counts, fp)
# %%
# train_word_counts = sort_dict_by_value(train_word_counts)

# %%
train_word_counts_1 = keys_by_value(train_word_counts)

# %%
unknown_dictionary = replace_dict_by_unknown(train_word_counts_1)
# %%
change_files_with_unknown_words(
    'docs\\brown_hw_lowercase\\Train\\', 'docs\\brown_hw_with_unk\\Train\\', unknown_dictionary)
# %%
train_root = 'docs\\brown_hw_with_unk\\Train'
train_reader = TaggedCorpusReader(train_root, '.*')
# %%
train_words = train_reader.words()

# %%
train_words
# %%
