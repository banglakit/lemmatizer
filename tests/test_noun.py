import pytest

from banglakit import lemmatizer


def test_return_whole_when_base_noun():
    assert lemmatizer.get('গাছ', pos=lemmatizer.POS_NOUN) == 'গাছ'


@pytest.mark.parametrize('inflected, lemmatized', [
    ('সদস্যবৃন্দ', 'সদস্য'),
    ('শিক্ষকমণ্ডলী', 'শিক্ষক'),
    ('পরিবারবর্গ', 'পরিবার'),
    ('পর্বতশ্রেণী', 'পর্বত'),
    ('পর্বতশ্রেনি', 'পর্বত'),
    ('পর্বতশ্রেণি', 'পর্বত'),
])
def test_strips_plural_from_inflected_noun(inflected, lemmatized):
    assert lemmatizer.get(inflected, pos=lemmatizer.POS_NOUN) == lemmatized


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
    assert lemmatizer.get(base, pos=lemmatizer.POS_NOUN) == base


def test_return_whole_when_proper_noun():
    assert lemmatizer.get('বাংলাদেশ', pos=lemmatizer.POS_PROPN) == 'বাংলাদেশ'


def test_dictionary_word():
    assert lemmatizer.get('অন্তর্জলি', pos=lemmatizer.POS_NOUN) == 'অন্তর্জলি'
