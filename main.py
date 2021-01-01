from helpers.extensions import load_multiple_corpus_files

train_set = load_multiple_corpus_files(
    "venv/nltk_data/corpora/brown_hw/Train/*")
test_set = load_multiple_corpus_files(
    "venv/nltk_data/corpora/brown_hw/Test/*")

print(train_set)
print(test_set)
