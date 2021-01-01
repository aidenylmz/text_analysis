import glob
import os
import nltk.data


def load_multiple_corpus_files(path):
    read_files = glob.glob(path + '*')

    with open("docs/result", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

    nltk_data = nltk.data.load('docs/result', format='raw')

    delete_file('docs/result')

    return nltk_data


def delete_file(full_path):
    if os.path.exists(full_path):
        os.remove(full_path)
