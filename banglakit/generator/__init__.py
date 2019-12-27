import itertools


def rule_1(base: str, root: str = None):
    rules = ['{r0}বেন', '{r1}েছেন', '{r1}েছিস', '{r0}িস', '{r0}ছে', '{r0}তেন', '{r0}ছিল', '{r1}েছিলি', '{r1}েছ',
             '{r0}ছেন', '{r0}ছিলে', '{r0}ত', '{r0}লেন', '{r1}েছি', '{r0}তে', '{r0}ছিস', '{r0}েন', '{r0}তাম', '{r0}লি',
             '{r1}েছিলাম', '{r0}', '{r0}বে', '{r0}ব', '{r0}ল', '{r1}েছে', '{r0}ছি', '{r0}লে', '{r0}ি', '{r0}ছিলেন',
             '{r0}বি', '{r1}েছিলে', '{r0}তি', '{r1}েছিল', '{r0}লাম', '{r0}ছিলি', '{r0}ছ', '{r1}েছিলেন', '{r0}ে',
             '{r0}ছিলাম']
    return {r.format(r0=base, r1=base.replace('া', 'ে')): root or base for r in rules}


def rule_2(base: str, root: str = None):
    rules = ['{r0}াচ্ছিলাম', '{r0}ালে', '{r0}ালি', '{r0}িয়েছিলি', '{r0}াচ্ছ', '{r0}িয়েছিল', '{r0}িয়েছি',
             '{r0}াতেন', '{r0}াচ্ছিলি', '{r0}াতে', '{r0}িয়েছিস', '{r0}াই', '{r0}াল', '{r0}িয়েছিলে', '{r0}ায়',
             '{r0}াবে', '{r0}াবি', '{r0}াচ্ছে', '{r0}াত', '{r0}িয়েছে', '{r0}া', '{r0}ালেন', '{r0}িয়েছেন',
             '{r0}াতাম', '{r0}াচ্ছি', '{r0}ান', '{r0}িয়েছিলাম', '{r0}াও', '{r0}াস', '{r0}াচ্ছিলে', '{r0}ালাম',
             '{r0}িয়েছিলেন', '{r0}াবেন', '{r0}াচ্ছেন', '{r0}াব', '{r0}াতি', '{r0}াচ্ছিলেন', '{r0}িয়েছ',
             '{r0}াচ্ছিস', '{r0}াচ্ছিল']
    return {r.format(r0=base, r1=base.replace('া', 'ে')): root or base for r in rules}


def generate_for(args, rules):
    d = {}
    for arg in args:
        for rule in rules:
            d.update(rule(arg, arg))

    return d


def generate():
    d = {}
    d.update(generate_for('কর গড় চর চড় ছড় ঝর নড় পর পড় ভর মর সর হাঁট কাট হাঁট ঘাট ছাট রাঁধ বাধ ছুট'.split(), [rule_1, rule_2]))
    d.update(generate_for('দৌড় ঝিম ঘুম চাল থাম কাম ঠেক পিট কিল ঘুষ লাত্থ'.split(), [rule_2]))

    return d
