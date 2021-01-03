import glob
import os


def delete_file(full_path):
    if os.path.exists(full_path):
        os.remove(full_path)


def lower_files(parent_path):
    read_files = glob.glob(parent_path + '*')

    for file in read_files:
        with open(file, "r") as infile:
            text = infile.read()

            lines = [text.lower() for line in file]
            with open(file, 'w') as out:
                out.writelines(lines)


def load_multiple_corpus_files(path):
    read_files = glob.glob(path + '*')

    sub_folder = path.split('\\')[-2]

    with open(f"docs/{sub_folder}.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                for line in infile:
                    line = line.lower()
                    outfile.write(line)
