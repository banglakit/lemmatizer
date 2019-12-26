# BanglaKit Lemmatizer

![Build Badge](https://github.com/banglakit/lemmatizer/workflows/banglakit-lemmatizer/badge.svg)

A rule-based lemmatizer for Bengali / Bangla based written in Python. Under active development.

## Installation

The package is still not mature. We are not on PyPI yet, install from GitHub for the time being!

```shell script
$ pip install git+https://github.com/banglakit/lemmatizer.git#egg=banglakit-lemmatizer
```

## Usage

```python

from banglakit import lemmatizer

lemmatizer.get('বাংলাদেশের', pos=lemmatizer.POS_PROPN)
# বাংলাদেশ

lemmatizer.get('বাংলাদেশের', pos='proper_noun')
# বাংলাদেশ
```