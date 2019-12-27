import pytest

from banglakit import lemmatizer as lem
from banglakit.lemmatizer import BengaliLemmatizer


def test_return_whole_when_base_noun():
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize('গাছ', pos=lem.POS_NOUN) == 'গাছ'


@pytest.mark.parametrize('inflected, lemmatized', [
    ('সদস্যবৃন্দ', 'সদস্য'),
    ('শিক্ষকমণ্ডলী', 'শিক্ষক'),
    ('পরিবারবর্গ', 'পরিবার'),
    ('পর্বতশ্রেণী', 'পর্বত'),
    ('পর্বতশ্রেনি', 'পর্বত'),
    ('পর্বতশ্রেণি', 'পর্বত'),
])
def test_strips_plural_from_inflected_noun(inflected, lemmatized):
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize(inflected, pos=lem.POS_NOUN) == lemmatized


@pytest.mark.parametrize('base,', [
    'ছড়া',
    'খান',
    'কুল',
    'কুল',
    'রাজি',
    'বর্গ',
    'বর্গ',
    'শ্রেণী',
])
def test_does_not_lemmatize_base_noun(base):
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize(base, pos=lem.POS_NOUN) == base


def test_return_whole_when_proper_noun():
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize('গাগাগুগুপাপাপুপুরে', pos=lem.POS_PROPN) == 'গাগাগুগুপাপাপুপুরে'


@pytest.mark.parametrize('word', ['অন্তর্জলি', 'চেহারা', 'আদুরে'])
def test_dictionary_word(word):
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize(word, pos=lem.POS_NOUN) == word


@pytest.mark.parametrize('inflected,lemmatized', [
    ('গিয়েছিল', 'যাওয়া'),
])
def test_lookup_table_used(inflected, lemmatized):
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize(inflected, pos=lem.POS_NOUN) == lemmatized
