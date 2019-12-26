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


def test_return_whole_when_proper_noun():
    assert lemmatizer.get('বাংলাদেশ', pos=lemmatizer.POS_PROPN) == 'বাংলাদেশ'
