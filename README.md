# BanglaKit Lemmatizer

A rule-based lemmatizer for Bengali / Bangla based written in Python. Under active development.

## Installation

The package is still not mature. We are not on PyPI yet, install from GitHub for the time being!

```shell script
$ pip install git+https://github.com/banglakit/lemmatizer.git#egg=banglakit-lemmatizer
```

## Usage

```python

from banglakit import lemmatizer

lemmatizer.get('বাংলাদেশের')
# বাংলাদেশ
```