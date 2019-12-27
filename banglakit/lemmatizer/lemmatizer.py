import json
import os
from typing import Dict, List, Set
from .consts import *

__all__ = ['BengaliLemmatizer']

# Data Paths
DEFAULT_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

RULES_FILE_PATH = os.path.join(DEFAULT_DATA_DIR, 'bn_lemma_rules.json')
WORD_LIST_PATH = os.path.join(DEFAULT_DATA_DIR, 'bn_words.json')
LOOKUP_TABLE_PATH = os.path.join(DEFAULT_DATA_DIR, 'bn_lemma_lookup.json')
LOOKUP_GENERATED_PATH = os.path.join(DEFAULT_DATA_DIR, 'bn_lemma_lookup_generated.json')
PRONOUN_LIST_PATH = os.path.join(DEFAULT_DATA_DIR, 'bn_pronoun_list.json')


class BengaliLemmatizer:
    def __init__(self, lemma_lookup: Dict[str, str] = None, lemma_rules: Dict[str, List[str]] = None,
                 pronoun_set: Set[str] = None, word_set: Set[str] = None):

        if not lemma_rules:
            lemma_rules = self._load_map(RULES_FILE_PATH)

        if not lemma_lookup:
            lemma_lookup = self._load_map(LOOKUP_TABLE_PATH)
            lemma_lookup.update(self._load_map(LOOKUP_GENERATED_PATH))

        if not pronoun_set:
            pronoun_set = self._load_set(PRONOUN_LIST_PATH)

        if not word_set:
            word_set = self._load_set(WORD_LIST_PATH)

        self.lemma_rules = lemma_rules
        self.lemma_lookup = lemma_lookup
        self.pronoun_set = pronoun_set
        self.word_set = word_set

    def _load_map(self, path: str):
        with open(path) as f:
            return json.load(f)

    def _load_set(self, path: str):
        with open(path) as f:
            return set(json.load(f))

    def _remove_inflection(self, word: str, pos=None):
        for suffix, replacement in self.lemma_rules.get(pos, []):
            if word.endswith(suffix) and len(suffix) < len(word):
                return word[:-len(suffix)]
        return word

    def lemmatize(self, word: str, pos=None):
        if pos == POS_PRON or word in self.pronoun_set:
            return '-PRON-'
        if word in self.lemma_lookup:
            return self.lemma_lookup[word]
        if word in self.word_set:
            return word
        return self._remove_inflection(word, pos)
