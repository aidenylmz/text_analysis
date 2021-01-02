import glob
import os
# import nltk.data


def load_multiple_corpus_files(path):
    read_files = glob.glob(path + '*')

    sub_folder = path.split('/')[-2]

    with open(f"docs/{sub_folder}/{sub_folder}.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                for line in infile:
                    line = line.lower()
                    outfile.write(line)

    # nltk_data = nltk.data.load('docs/result', format='raw')

    # delete_file('docs/result')

    # return nltk_data


def delete_file(full_path):
    if os.path.exists(full_path):
        os.remove(full_path)
