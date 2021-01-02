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
