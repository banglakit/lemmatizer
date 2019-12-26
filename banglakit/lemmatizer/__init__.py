import json
import os

POS_NOUN = 'noun'
POS_PROPN = 'proper_noun'
POS_VERB = 'verb'

rules_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'bn_lemma_rules.json')
word_list_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'bn_lemma_rules.json')

with open(rules_path) as rules_file:
    RULES = json.load(rules_file)

with open(word_list_path) as rules_file:
    WORDS = set(json.load(rules_file))


def remove_inflection(word, pos=None):
    for suffix, replacement in RULES[pos]:
        if word.endswith(suffix) and len(suffix) < len(word):
            return word[:-len(suffix)]
    return word


def get(word: str, pos=None):
    if word in WORDS:
        return word
    if pos in RULES:
        return remove_inflection(word, pos)
    return word
