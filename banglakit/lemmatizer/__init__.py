import json
import os

POS_NOUN = 'noun'
POS_PROPN = 'proper_noun'
POS_VERB = 'verb'

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'bn_lemma_rules.json')

with open(path) as rules_file:
    RULES = json.load(rules_file)


def remove_inflection(word, pos=None):
    for suffix, replacement in RULES[pos]:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def get(word: str, pos=None):
    if pos in RULES:
        return remove_inflection(word, pos)
    return word
