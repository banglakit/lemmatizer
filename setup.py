from distutils.core import setup

setup(
    name='banglakit-lemmatizer',
    version='0.0.1',
    packages=['banglakit.lemmatizer'],
    url='https://github.com/banglakit/lemmatizer',
    license='MIT',
    author='The BanglaKit Project and Contributors',
    author_email='hi@banglakit.org',
    description='A rule-based Lemmatizer for Bengali',
    package_data={'banglakit.lemmatizer': ['data/*.json']}
)
