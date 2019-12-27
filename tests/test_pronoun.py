import pytest

from banglakit import lemmatizer


@pytest.mark.parametrize('pronoun', [
    'আমি', 'তুমি', 'সে', 'তিনি', 'তাদেরকে', 'যাদেরকে'
])
def test_pos_pronoun_replaced_with_placeholder(pronoun):
    assert lemmatizer.get(pronoun, pos=lemmatizer.POS_PRON) == '-PRON-'


@pytest.mark.parametrize('pronoun', [
    'আমি', 'তুমি', 'সে', 'তিনি', 'তাদেরকে', 'যাদেরকে'
])
def test_enlisted_pronoun_without_pos_replaced_with_placeholder(pronoun):
    assert lemmatizer.get(pronoun) == '-PRON-'
