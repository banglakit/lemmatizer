import json
import os

POS_NOUN = 'noun'
POS_PROPN = 'proper_noun'
POS_PRON = 'pronoun'
POS_VERB = 'verb'

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
RULES_FILE_PATH = os.path.join(DATA_DIR, 'bn_lemma_rules.json')
WORD_LIST_PATH = os.path.join(DATA_DIR, 'bn_words.json')
LOOKUP_TABLE_PATH = os.path.join(DATA_DIR, 'bn_lemma_lookup.json')
PRONOUN_LIST_PATH = os.path.join(DATA_DIR, 'bn_pronoun_list.json')

with open(RULES_FILE_PATH) as rules_file:
    RULES = json.load(rules_file)

with open(WORD_LIST_PATH) as word_list_file:
    WORDS = set(json.load(word_list_file))

with open(LOOKUP_TABLE_PATH) as lookup_table_file:
    LOOKUPS = json.load(lookup_table_file)

with open(PRONOUN_LIST_PATH) as pronoun_list_file:
    PRONOUNS = set(json.load(pronoun_list_file))


def remove_inflection(word, pos=None):
    for suffix, replacement in RULES.get(pos, []):
        if word.endswith(suffix) and len(suffix) < len(word):
            return word[:-len(suffix)]
    return word


def get(word: str, pos=None):
    if pos == POS_PRON or word in PRONOUNS:
        return '-PRON-'
    if word in LOOKUPS:
        return LOOKUPS[word]
    if word in WORDS:
        return word
    return remove_inflection(word, pos)
