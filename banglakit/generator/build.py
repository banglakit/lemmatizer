import json
import os

from banglakit.generator import generate

this_dir = os.path.dirname(os.path.realpath(__file__))
lemmatizer_dir = os.path.join(this_dir, '..', 'lemmatizer', 'data')
out_file = os.path.join(lemmatizer_dir, 'bn_lemma_lookup_generated.json')

with open(out_file, 'w') as f:
    json.dump(generate(), f, ensure_ascii=False, indent=2)
