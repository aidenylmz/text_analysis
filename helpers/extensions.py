import glob
import os


def delete_file(full_path):
    if os.path.exists(full_path):
        os.remove(full_path)


def lower_files(parent_path, write_path):
    read_files = glob.glob(parent_path + '*')

    for file in read_files:
        with open(file, "r") as infile:
            file_name = os.path.basename(infile.name)
            text = infile.read()
        with open(write_path + file_name, 'w') as out:
            out.write(text.lower())


def load_multiple_corpus_files(path):
    read_files = glob.glob(path + '*')

    sub_folder = path.split('\\')[-2]

    with open(f"docs/{sub_folder}.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                for line in infile:
                    line = line.lower()
                    outfile.write(line)


def sort_dict_by_value(dictionary: dict, descending=True):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=descending)}


def count_keys_by_value(dictionary, value=1):
    res = 0
    for key in dictionary:
        if dictionary[key] == value:
            res = res + 1

    return res


def keys_by_value(dictionary, value=1):
    res = {}
    for word, count in dictionary.items():
        if count == value:
            res[word] = count

    return res


def replace_dict_by_unknown(dictionary, value=1):
    res = {}
    for word in dictionary.keys():
        res[word] = 'UNK'

    return res


def change_files_with_unknown_words(parent_path, write_path, unknown_dictionary):
    read_files = glob.glob(parent_path + '*')

    for file in read_files:
        with open(file, "r") as infile:
            file_name = os.path.basename(infile.name)
            text = infile.read()

        for word in unknown_dictionary.keys():
            if text.find(word) >= 0:
                text = keymap_replace(text, unknown_dictionary)

        with open(write_path + file_name, 'w') as out:
            out.write(text)


def keymap_replace(
    string: str,
    mappings: dict,
    lower_keys=False,
    lower_values=False,
    lower_string=False,
) -> str:
    """Replace parts of a string based on a dictionary.

    This function takes a string a dictionary of
    replacement mappings. For example, if I supplied
    the string "Hello world.", and the mappings 
    {"H": "J", ".": "!"}, it would return "Jello world!".

    Keyword arguments:
    string       -- The string to replace characters in.
    mappings     -- A dictionary of replacement mappings.
    lower_keys   -- Whether or not to lower the keys in mappings.
    lower_values -- Whether or not to lower the values in mappings.
    lower_string -- Whether or not to lower the input string.
    """
    replaced_string = string.lower() if lower_string else string
    for character, replacement in mappings.items():
        replaced_string = replaced_string.replace(
            character.lower() if lower_keys else character,
            replacement.lower() if lower_values else replacement
        )
    return replaced_string
