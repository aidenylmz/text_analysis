
# from helpers.extensions import load_multiple_corpus_files
from nltk.corpus.reader.tagged import TaggedCorpusReader
import nltk
from helpers.extensions import sort_dict_by_value, keys_by_value


# Lower cases the files and saves it to another location
# lower_files('docs\\brown_hw\\Train\\', 'docs\\brown_hw_lowercase\\Train\\')
# lower_files('docs\\brown_hw\\Test\\', 'docs\\brown_hw_lowercase\\Test\\')

# load_multiple_corpus_files('docs\\brown_hw\\Train\\')
# load_multiple_corpus_files('docs\\brown_hw\\Test\\')


# TaggedCorpusReader for train set
train_root = 'docs\\brown_hw_lowercase\\Train'
train_reader = TaggedCorpusReader(train_root, '.*')

train_words = train_reader.words()

train_word_counts = nltk.FreqDist(train_words)

# Words of train set that occurs only once
train_word_counts_1 = keys_by_value(train_word_counts)

# Words with tags of train set
tagged_words_with_unk = [list(x) for x in train_reader.tagged_words()]

# Makes words 'UNK' whose counts are one
for index, tagged_word in enumerate(tagged_words_with_unk):
    if tagged_word[0] in train_word_counts_1.keys():
        tagged_words_with_unk[index][0] = 'UNK'

# Computes tag frequencies and put them into dictionary
tag_frequency = {}
for index, tagged_word in enumerate(tagged_words_with_unk):
    try:
        tag_frequency[tagged_word[1]] += 1
    except KeyError:
        tag_frequency[tagged_word[1]] = 1


# Sorted tag frequency dictionary
tag_frequency = sort_dict_by_value(tag_frequency)

# Write sorted tag frequency to a file
with open('docs\\PosTags.txt', 'w') as pos_tags_file:
    pos_tags_file.write('Tag | Tag Frequency\n')
    for tag, frequency in tag_frequency.items():
        pos_tags_file.write(f'{tag} | {frequency}\n')


# Transition Counts
train_transition_counts = {}
for index, tagged_word in enumerate(tagged_words_with_unk):
    taga = tagged_words_with_unk[index][1]
    try:
        tagb = tagged_words_with_unk[index+1][1]
    except IndexError:
        break
    tag_pairs = (taga, tagb)
    try:
        train_transition_counts[tag_pairs] += 1
    except KeyError:
        train_transition_counts[tag_pairs] = 1

train_transition_counts = sort_dict_by_value(train_transition_counts)

# Transition Probability
train_transition_probabilities = {}
for transition, count in train_transition_counts.items():
    probability = train_transition_counts[transition] / \
        tag_frequency[transition[0]]
    train_transition_probabilities[transition] = probability


# Sorted transition probabilities alphabetically
sorted_train_transition_probs = sorted(train_transition_probabilities.items())

# Write sorted transition probability of tags to a file
with open('docs\\TransitionProbs.txt', 'w') as transition_probs_file:
    transition_probs_file.write('TagA | TagB | P(tagb|taga)\n')
    for elements in sorted_train_transition_probs:
        transition_probs_file.write(
            f'{elements[0][0]} | {elements[0][1]} | {elements[1]}\n')

# Word - Tag Pair Counts
word_tag_count = {}
for index, tagged_word in enumerate(tagged_words_with_unk):
    try:
        word_tag_count[tuple(tagged_word)] += 1
    except KeyError:
        word_tag_count[tuple(tagged_word)] = 1

# Emission Probability
train_emission_probabilities = {}
for word_tag, count in word_tag_count.items():
    probability = count / \
        tag_frequency[word_tag[1]]
    train_emission_probabilities[word_tag] = probability

# Sorted emission probabilities alphabetically
sorted_train_emission_probs = sorted(train_emission_probabilities.items())

# Write sorted emission probability of tags to a file and vocabulary with most likely tag
# previous word and probability are declared for better find performance for optimization
previous_word = sorted_train_emission_probs[0][0][0]
biggest_probability = sorted_train_emission_probs[0][1]
words_most_likely_tags = {}

with open('docs\\EmissionProbs.txt', 'w') as emission_probs_file:
    emission_probs_file.write('Tag | Kelime | P(kelime|tag)\n')
    for elements in sorted_train_emission_probs:
        word = elements[0][0]
        tag = elements[0][1]
        prob = elements[1]
        if word == previous_word:
            if prob > biggest_probability:
                words_most_likely_tags[word] = prob
                biggest_probability = prob
            else:
                words_most_likely_tags[word] = biggest_probability
        else:
            words_most_likely_tags[word] = prob
            previous_word = word
            biggest_probability = prob

        emission_probs_file.write(
            f'{tag} | {word} | {prob}\n')

# All words with UNK
train_words_with_unknown = []
for index, word in enumerate(train_words):
    if word in train_word_counts_1.keys():
        train_words_with_unknown.append('UNK')
    else:
        train_words_with_unknown.append(word)

# Word frequency with UNK
word_frequency = {}
for index, word in enumerate(train_words_with_unknown):
    try:
        word_frequency[word] += 1
    except KeyError:
        word_frequency[word] = 1

# Write vocabulary.txt
with open('docs\\Vocabulary.txt', 'w') as vocab_file:
    vocab_file.write('Kelime | Kelimenin Frekansi | Most Likely Tag\n')
    for word, mlt in words_most_likely_tags.items():
        frequency = word_frequency[word]
        vocab_file.write(
            f'{word} | {frequency} | {mlt}\n')


# Initial Probs
train_initial_probs = {}
for pair, count in train_transition_counts.items():
    if pair[0] == '.':
        probability = count / \
            tag_frequency[pair[1]]
        train_initial_probs[pair[1]] = probability


sorted_train_initial_probs = sorted(train_initial_probs.items())

# Initial Prob write
with open('docs\\InitialProbs.txt', 'w') as initial_probs_file:
    initial_probs_file.write('Tag | P(tag|<s>)\n')
    for elements in sorted_train_initial_probs:
        initial_probs_file.write(
            f'{elements[0]} | {elements[1]}\n')
