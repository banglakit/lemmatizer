import pytest

from banglakit import lemmatizer as lem
from banglakit.lemmatizer import BengaliLemmatizer


@pytest.mark.parametrize('pronoun', [
    'আমি', 'তুমি', 'সে', 'তিনি', 'তাদেরকে', 'যাদেরকে'
])
def test_pos_pronoun_replaced_with_placeholder(pronoun):
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize(pronoun, pos=lem.POS_PRON) == '-PRON-'


@pytest.mark.parametrize('pronoun', [
    'আমি', 'তুমি', 'সে', 'তিনি', 'তাদেরকে', 'যাদেরকে'
])
def test_enlisted_pronoun_without_pos_replaced_with_placeholder(pronoun):
    lemmatizer = BengaliLemmatizer()
    assert lemmatizer.lemmatize(pronoun) == '-PRON-'
