import re


def rule_1(base: str):
    rules = ['{r0}বেন', '{r1}েছেন', '{r1}েছিস', '{r0}িস', '{r0}ছে', '{r0}তেন', '{r0}ছিল', '{r1}েছিলি', '{r1}েছ',
             '{r0}ছেন', '{r0}ছিলে', '{r0}ত', '{r0}লেন', '{r1}েছি', '{r0}তে', '{r0}ছিস', '{r0}েন', '{r0}তাম', '{r0}লি',
             '{r1}েছিলাম', '{r0}', '{r0}বে', '{r0}ব', '{r0}ল', '{r1}েছে', '{r0}ছি', '{r0}লে', '{r0}ি', '{r0}ছিলেন',
             '{r0}বি', '{r1}েছিলে', '{r0}তি', '{r1}েছিল', '{r0}লাম', '{r0}ছিলি', '{r0}ছ', '{r1}েছিলেন', '{r0}ে',
             '{r0}ছিলাম']
    return {r.format(r0=base, r1=base.replace('া', 'ে')) for r in rules}


RULES = [
    (re.compile(r'.*াট$'), rule_1)
]


def generate(base: str):
    for matcher, rule in RULES:
        if matcher.match(base):
            return rule(base)

    return {base}


